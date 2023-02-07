from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly 
from app_auth.serializers import UserSerializer , PermissionSerializer
from app_auth.models import User
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Permission


class UserListCreateView(ListCreateAPIView):
    permission_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PermissionListCreateApiView(ListCreateAPIView):
    permission_classes = []
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()


class UserPermissionListcreateApiView(ListCreateAPIView):
    permission_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def get(self, request, *args, **kwargs):
        print(request.user.user_permissions.all())
        print(request.user)
        return self.list(request, *args, **kwargs)
    

# def test(request):
#     query = Permission.objects.get(codename='add_logentry')
#     print('query ', query)
#     request.user.user_permissions.add(query)
#     print(request.user)
#     return HttpResponse('hello')
