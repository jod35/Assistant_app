# from rest_framework import serializers
# from rest_framework.authtoken.models import Token
# from rest_framework.validators import ValidationError

# #from .models import User
# from django.contrib.auth.models import User



# class SignUpSerializer(serializers.ModelSerializer):
#     email = serializers.CharField(max_length=80)
#     username = serializers.CharField(max_length=45)
#     password = serializers.CharField(min_length=8, write_only=True)

#     class Meta:
#         model = User
#         fields = ["email", "username", "password"]

#     def validate(self, attrs):

#         email_exists = User.objects.filter(email=attrs["email"]).exists()

#         if email_exists:
#             raise ValidationError("Email has already been used")

#         return super().validate(attrs)

#     def create(self, validated_data):
#         password = validated_data.pop("password")

#         user = super().create(validated_data)

#         user.set_password(password)

#         user.save()

#         Token.objects.create(user=user)

#         return user


# class CurrentUserPostsSerializer(serializers.ModelSerializer):
#     posts = serializers.HyperlinkedRelatedField(
#         many=True, view_name="post_detail", queryset=User.objects.all()
#     )

#     class Meta:
#         model = User
#         fields = ["id", "username", "email", "posts"]

from rest_framework.authtoken.models import Token

from rest_framework.validators import ValidationError

from rest_framework import serializers

from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    phone = serializers.IntegerField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'password']

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
