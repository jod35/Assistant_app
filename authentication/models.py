from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Manager for users
class UserProfileManager(BaseUserManager):
    def create_superuser(self, first_name, last_name, email, phone, date_of_birth, password):
        if not email or not first_name or not last_name or not phone or not date_of_birth:
            raise ValueError('All fields are required')

        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, phone=phone, email=email, date_of_birth=date_of_birth)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=80, unique=True)
    phone = models.IntegerField()
    username = None
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    password = models.CharField(max_length=200)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'date_of_birth', 'password']

    class Meta:
        verbose_name_plural = 'users'
        db_table = 'users'

    def __str__(self):
        return str(self.username)


class Profile(models.Model):
    pass