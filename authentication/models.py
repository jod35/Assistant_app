from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=80, unique=True)
    address = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    username = None
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    password = models.CharField(max_length=200)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
    'first_name', 
    'last_name', 
    'address',
    'zip_code', 
    'date_of_birth', 
    'password']

    class Meta:
        verbose_name_plural = 'users'
        db_table = 'users'

    def __str__(self):
        return str(self.username)


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
