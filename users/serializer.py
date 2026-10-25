from .models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken  

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "password",
        ]
    def create(self, validated_data):
        new_user = User.objects.create_user(**validated_data)
        return new_user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(
            username=username,
            password=password,
        )
        if user is None:
            raise serializers.ValidationError(
                "نام کاربری یا رمز عبور اشتباه است"
            )

        if not user.is_active:
            raise serializers.ValidationError(
                "حساب کاربری غیرفعال است"
            )

        refresh = RefreshToken.for_user(user)
        attrs["user"] = user
        attrs["refresh"] = str(refresh)
        attrs["access"] = str(refresh.access_token)

        return attrs
    


