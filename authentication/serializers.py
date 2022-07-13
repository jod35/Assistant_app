from rest_framework.authtoken.models import Token

from rest_framework.validators import ValidationError

from rest_framework import serializers

from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    # Check if email already exists in database
    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise ValidationError('Email already exists, please login')

        return super().validate(attrs)


    # Encrypt the password before creating the user
    def create(self, validated_data):
        password = validated_data.pop('password')

        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        return user

# serializer for updating user
class UserSerializer(serializers.ModelSerializer):
    class meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'Address', 'zip_code' 'password']




