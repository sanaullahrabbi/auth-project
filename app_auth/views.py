from django.contrib.auth.models import Group, Permission
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail


from app_auth.models import Role, User
from app_auth.serializers import (ChangePasswordSerializer, EmailSerializer,
                                  GroupSerializer, PermissionSerializer,
                                  ResetPasswordSerializer, RoleSerializer,
                                  UserGroupSerializer,
                                  UserPermissionSerializer, UserSerializer)


# USER ROLE
class UserRoleListCreateView(ListCreateAPIView):
    permission_classes = []
    serializer_class = RoleSerializer
    queryset = Role.objects.all()


# USER
class UserListCreateView(ListCreateAPIView):
    permission_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()


# CHANGE PASSWORD
class ChangePasswordView(UpdateAPIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except Exception as e:
            return Response({"message": str(e)})

    def update(self, request, pk, *args, **kwargs):
        user = self.get_object(pk)
        serializer = ChangePasswordSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"message": "Password changed successfully."}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# USER PERMISSION
class UserPermissionListCreateView(ListCreateAPIView):
    permission_classes = []
    serializer_class = UserPermissionSerializer
    queryset = User.objects.all()


class UserPermissionRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class = UserPermissionSerializer
    queryset = User.objects.all()


# USER GROUPS
class UserGroupListCreateView(ListCreateAPIView):
    permission_classes = []
    serializer_class = UserGroupSerializer
    queryset = User.objects.all()


class UserGroupRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class = UserGroupSerializer
    queryset = User.objects.all()


# GROUPS
class GroupListCreateView(ListCreateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class GroupUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    lookup_field = "id"


# PERMISSIONS
class PermissionListCreateApiView(ListCreateAPIView):
    permission_classes = []
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()


# --- Reset Password ---


class PasswordReset(APIView):
    serializer_class = EmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        user = User.objects.filter(email=email).first()
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = reverse(
                "app_auth:reset-password",
                kwargs={"encoded_pk": encoded_pk, "token": token},
            )
            reset_link = f"Hello, We recived a request to reset the password for yout account for this email address.Clik the link & to set a new password. http://127.0.0.1:8000{reset_url}"

            send_mail(
            'Your Forget Password', 
            reset_link,
            'mdalaminislam.pro@gmail.com', 
            [user.email], 
            )

            return Response(
                {
                    "message":
                    f"Your password rest link: {reset_link}"
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "User doesn't exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ResetPasswordAPI(APIView):
    serializer_class = ResetPasswordSerializer

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )
def test(request):
    return render(request, "index.html", context={})

# def test(request):
#     send_mail(
#     'Subject here', 
#     'Here is the message.', 
#     'mdalaminislam.pro@gmail.com', 
#     ['mdalaminislam.py@gmail.com'], 
#     # fail_silently=False,
#     )
#     return HttpResponse("hello")