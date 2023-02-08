from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Role(models.Model):
    """
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    """

    USER = 1
    ADMIN = 2
    ROLE_CHOICES = (
        (USER, "user"),
        (ADMIN, "admin"),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class User(AbstractUser):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others"),
    )
    full_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, null=True, blank=True, max_length=7
    )
    image = models.ImageField(
        upload_to="profile_picture/%Y/%d/%b", null=True, blank=True
    )

    roles = models.ManyToManyField(Role, blank=True)

    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.full_name = self.get_full_name()
        super().save(*args, **kwargs)

    def update_is_role(self):
        if hasattr(self, "roles"):
            for role in self.roles.all():
                if role.id == Role.USER:
                    self.is_user = True

                elif role.id == Role.ADMIN:
                    self.is_admin = True

    def recheck_is_role(self):
        if hasattr(self, "roles"):
            roles = self.roles.all()
            if roles:
                if self.is_user == True:
                    if not roles.filter(id=Role.USER).exists():
                        self.is_user = False

                if self.is_admin == True:
                    if not roles.filter(id=Role.ADMIN).exists():
                        self.is_admin = False
            else:
                self.is_user = False
                self.is_admin = False


class Address(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user_address",
    )
    full_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    street_address = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"User: {self.user}-{self.street_address}"
