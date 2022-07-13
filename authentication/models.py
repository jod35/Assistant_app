# from django.db import models

# from django.contrib.auth.models import (BaseUserManager, AbstractUser)


# # Manager for users
# class UserProfileManager(BaseUserManager):
#     def create_superuser(self, first_name, last_name, email, Address, password):
#         if not email or not first_name or not last_name or not Address:
#             raise ValueError('All fields are required')

#         email = self.normalize_email(email)
#         user = self.model(first_name=first_name, last_name=last_name, email=email)
#         user.set_password(password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()

#         return user


# # Database model for users
# class User(AbstractUser):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     Address = models.CharField(max_length=75, default='test')
#     zip_code = models.IntegerField(default='1')
#     city_name = models.CharField(max_length=50, default='test')
#     username = None
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     updated_at = models.DateField(auto_now=True)
#     password = models.CharField(max_length=150)

#     objects = UserProfileManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'Address', 'zip_code', 'city_name', 'password']
    

#     class Meta:
#         verbose_name_plural = 'users'
#         db_table = 'users'

#     def __str__(self):
#         return self.email

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     alias_name = models.CharField(max_length=100)
#     profile_text = models.CharField(max_length=255)
#     profile_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

#     class Meta:
#         verbose_name_plural = 'Profile'
#         db_table = 'Profile'

#     def __str__(self):
#         return self.email


# """
# #creating a custom user model
# - AbstractUser (this works with django's default user model)
# - AbstractBaseUser (this woks when building from scratch)


# """
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    email = models.CharField(max_length=80, unique=True)
    username = models.CharField(max_length=45)
    date_of_birth = models.DateField(null=True)
    Address = models.CharField(max_length=75, default='test')
    zip_code = models.IntegerField(default='1')
    city_name = models.CharField(max_length=50, default='test')


    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alias_name = models.CharField(max_length=100)
    profile_text = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name_plural = 'Profile'
        db_table = 'Profile'

    def __str__(self):
        return self.email