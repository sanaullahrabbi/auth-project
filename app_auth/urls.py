from django.urls import path

from app_auth.views import (
    ChangePasswordView,
    GroupListCreateView,
    GroupUpdateDeleteView,
    PermissionListCreateApiView,
    UserGroupListCreateView,
    UserGroupRetriveUpdateDeleteView,
    UserListCreateView,
    UserPermissionListCreateView,
    UserPermissionRetriveUpdateDeleteView,
    UserRetriveUpdateDeleteView,
    UserRoleListCreateView,
    PasswordReset,
    ResetPasswordAPI,
    test,
)

app_name = "app_auth"

urlpatterns = [
    path("users/", UserListCreateView.as_view(), name="users_list_create"),
    path(
        "users/<int:pk>/",
        UserRetriveUpdateDeleteView.as_view(),
        name="users_retrive_update_delete",
    ),
    path("user-roles/", UserRoleListCreateView.as_view(), name="user_role_list_create"),
    path(
        "permissions/",
        PermissionListCreateApiView.as_view(),
        name="permission_list_create",
    ),
    path(
        "user-permissions/",
        UserPermissionListCreateView.as_view(),
        name="permission_list_create",
    ),
    path(
        "user-permissions/<int:pk>/",
        UserPermissionRetriveUpdateDeleteView.as_view(),
        name="permission_retrive_update_delete",
    ),
    path(
        "user-groups/",
        UserGroupListCreateView.as_view(),
        name="group_list_create",
    ),
    path(
        "user-groups/<int:pk>/",
        UserGroupRetriveUpdateDeleteView.as_view(),
        name="group_retrive_update_delete",
    ),
    path("groups/", GroupListCreateView.as_view(), name="group_list_create"),
    path(
        "groups/<int:pk>",
        GroupUpdateDeleteView.as_view(),
        name="group_update_delete",
    ),
    path(
        "user-change-password/<int:pk>/",
        ChangePasswordView.as_view(),
        name="users_change_password",
    ),
    # --- Reset Password ---
    path(
        "password-reset/",
        PasswordReset.as_view(),
        name="request-password-reset",
    ),
    path(
        "password-reset/<str:encoded_pk>/<str:token>/",
        ResetPasswordAPI.as_view(),
        name="reset-password",
    ),
    path("test/", test),
]
