from django.db import models

from django.contrib.auth.models import (BaseUserManager, AbstractUser)


# Manager for users
class UserProfileManager(BaseUserManager):
    def create_superuser(self, first_name, last_name, email, Address, password):
        if not email or not first_name or not last_name or not Address:
            raise ValueError('All fields are required')

        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


# Database model for users
class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    Address = models.CharField(max_length=75, default='test')
    zip_code = models.IntegerField(default='1')
    city_name = models.CharField(max_length=50, default='test')
    username = None
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
    password = models.CharField(max_length=150)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'Address', 'zip_code', 'city_name', 'password']
    

    class Meta:
        verbose_name_plural = 'users'
        db_table = 'users'

    def __str__(self):
        return self.email

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
