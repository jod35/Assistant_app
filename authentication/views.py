from urllib import response
from django.contrib.auth import authenticate
from django.shortcuts import render
from fastapi import Depends
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .serializers import SignUpSerializer, UserSerializer
from .tokens import create_jwt_pair_for_user


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "User Created Successfully", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:

            tokens = create_jwt_pair_for_user(user)

            response = {"message": "Login Successfull", "tokens": tokens}
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Invalid email or password"})

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)


# Read user data
@api_view(http_method_names=['GET'])
def read_user(request:Request):
    user = user.objects.filter(email=request.user)
    serializer = UserSerializer(instance=user, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)



@api_view(http_method_names=['PUT'])
def update_user(request=Request):
    data = request.data

    serializer = UserSerializer(instance=request.user, data=data)

    if serializer.is_valid():
        serializer.save()

    response = {
        'message': 'User updated succsesfully',
        'data': serializer.data
    }


    return Response(data=response, status=status.HTTP_200_OK)