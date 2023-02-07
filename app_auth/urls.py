from django.urls import path
from app_auth.views import UserListCreateView, UserRetriveUpdateDeleteView

app_name = 'app_auth'

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='users_list_create'),
    path('users/<int:pk>/', UserRetriveUpdateDeleteView.as_view(), name='users_retrive_update_delete'),
]
