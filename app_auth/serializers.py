from django.contrib.auth.models import Group, Permission
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers
from app_auth.models import Role, User


class RoleSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = Role
        fields = "__all__"

    def get_role(self, obj):
        return obj.get_id_display()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {
                "write_only": True,
                "required": False,
            },
        }

    def validate(self, data):
        password = data.get("password", None)
        print(password)
        if not self.instance and not password:
            raise serializers.ValidationError(
                {"password": ["The password is required on user profile creation."]}
            )

        return super().validate(data)

    def validate_password(self, value):
        print("test")
        if not self.instance and not value:
            raise serializers.ValidationError(
                "The password is required on user profile creation."
            )

        return value

    def create(self, validated_data):
        roles = validated_data.pop("roles")
        user = User.objects.create_user(**validated_data)
        user.roles.add(*roles)
        user.update_is_role()
        user.recheck_is_role()
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.update_is_role()
        user.recheck_is_role()
        user.save()
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    re_new_password = serializers.CharField(required=True, write_only=True)

    def update(self, instance, validated_data):
        instance.password = validated_data.get("password", instance.password)

        if not validated_data["new_password"]:
            raise serializers.ValidationError({"new_password": "not found"})

        if not validated_data["old_password"]:
            raise serializers.ValidationError({"old_password": "not found"})

        if not instance.check_password(validated_data["old_password"]):
            raise serializers.ValidationError({"old_password": "wrong password"})

        if validated_data["new_password"] != validated_data["re_new_password"]:
            raise serializers.ValidationError({"passwords": "passwords do not match"})

        if validated_data["new_password"] == validated_data[
            "re_new_password"
        ] and instance.check_password(validated_data["old_password"]):
            instance.set_password(validated_data["new_password"])
            instance.save()
            return instance


class UserPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "user_permissions",
        )


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "groups",
        )


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"



class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ("email",)


class ResetPasswordSerializer(serializers.Serializer):

    password = serializers.CharField(
        write_only=True,
        min_length=1,
    )

    class Meta:
        field = ("password")

    def validate(self, data):
        password = data.get("password")
        token = self.context.get("kwargs").get("token")
        encoded_pk = self.context.get("kwargs").get("encoded_pk")

        if token is None or encoded_pk is None:
            raise serializers.ValidationError("Missing data.")

        pk = urlsafe_base64_decode(encoded_pk).decode()
        user = User.objects.get(pk=pk)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError("The reset token is invalid")

        user.set_password(password)
        user.save()
        return data