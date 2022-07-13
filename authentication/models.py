from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.CharField(max_length=80, unique=True)
    username = models.CharField(max_length=45)
    date_of_birth = models.DateField(null=True)
    Address = models.CharField(max_length=75, default='test')
    zip_code = models.IntegerField(default='1')
    city_name = models.CharField(max_length=50, default='test')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'Address', 'zip_code', 'city_name', 'password']
    

    class Meta:
        verbose_name_plural = 'users'
        db_table = 'users'

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
