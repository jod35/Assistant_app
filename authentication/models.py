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