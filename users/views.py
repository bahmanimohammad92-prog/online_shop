from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer, LoginSerializer
from rest_framework import status

class SignupAPIView(APIView):
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            created_user = serializer.save()
            return Response(
                {
                    "message": "ثبت نام با موفقیت انجام شده است",
                    "user": {
                        "id": created_user.id,
                        "username": created_user.username,
                        "email": created_user.email,

                    }
                },
                status=status.HTTP_201_CREATED
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    
    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                {
                    "message": "ورود با موفقیت انجام شده است",
                    "access": serializer.validated_data["access"],
                    "refresh": serializer.validated_data["refresh"],
                    "user": {
                        "id": serializer.validated_data["user"].id,
                        "username": serializer.validated_data["user"].username,
                    }
                },
                status=status.HTTP_200_OK
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


