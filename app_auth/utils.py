from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404

def user_gains_perms(request, user_id, codename):
    user = get_object_or_404(User, pk=user_id)
    user.has_perm('app_auth.change_userpost')
    permission = Permission.objects.get(
        codename = codename
    )
    user.user_permissions.add(permission)