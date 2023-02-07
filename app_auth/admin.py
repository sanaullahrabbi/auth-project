from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app_auth.models import User

from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = (
        "username",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "username",
        "is_staff",
        "is_active",
    )
    # fieldsets = (
    #     (None, {"fields": ("email", "password")}),
    #     ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         "classes": ("wide",),
    #         "fields": (
    #             "email", "password1", "password2", "is_staff",
    #             "is_active", "groups", "user_permissions"
    #         )}
    #     ),
    # )
    search_fields = ("username","email")
    ordering = ("username","email",)


admin.site.register(User, CustomUserAdmin)
