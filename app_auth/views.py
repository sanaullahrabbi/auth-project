from django.contrib.auth.models import Group, Permission
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from app_auth.models import Role, User
from app_auth.serializers import (
    ChangePasswordSerializer,
    GroupSerializer,
    PermissionSerializer,
    RoleSerializer,
    UserGroupSerializer,
    UserPermissionSerializer,
    UserSerializer,
)


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


def test(request):
    return render(request, "index.html", context={})
