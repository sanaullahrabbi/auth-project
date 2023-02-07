from django.urls import path
from app_auth.views import UserListCreateView, UserRetriveUpdateDeleteView, PermissionListCreateApiView, UserPermissionListcreateApiView


app_name = 'app_auth'

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='users_list_create'),
    path('users/<int:pk>/', UserRetriveUpdateDeleteView.as_view(), name='users_retrive_update_delete'),
    path('permissions/', PermissionListCreateApiView.as_view(), name='permission_list_create'),
    path('user-permission/', UserPermissionListcreateApiView.as_view(), name='permission_list_create'),
    #path('test/', test)
]
