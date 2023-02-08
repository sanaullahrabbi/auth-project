from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly 
from app_auth.serializers import UserSerializer, ChangePasswordSerializer , PermissionSerializer
from app_auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Permission
from django.shortcuts import render


class UserListCreateView(ListCreateAPIView):
    permission_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def get(self, request, *args, **kwargs):
        print(self.queryset.first().roles.all())
        return self.list(request, *args, **kwargs)


class UserRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = UserSerializer
    queryset = User.objects.all()



class ChangePasswordView(UpdateAPIView):

    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except Exception as e:
            return Response({'message':str(e)})

    def update(self, request, pk, *args, **kwargs):
        user = self.get_object(pk) 
        serializer = ChangePasswordSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
             serializer.save()
             return Response({'message':'Password changed successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserView(UpdateAPIView):
#     serializer_class = serializers.UserSer
#     queryset = models.User.objects.all()

#     def get_object(self,pk):
#         try:
#             return models.User.objects.get(pk=pk)
#         except Exception as e:
#             return Response({'message':str(e)})

#     def put(self,request,pk,format=None):
#         user = self.get_object(pk) 
#         serializer = self.serializer_class(user,data=request.data)

#         if serializer.is_valid():            
#             serializer.save()
#             user.set_password(serializer.data.get('password'))
#             user.save()
#             return Response(serializer.data)    
#         return Response({'message':True})
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

def test(request):
    return render(request, 'index.html', context={})