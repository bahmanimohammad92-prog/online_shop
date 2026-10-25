from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(
        max_length=15
        )
    role = models.CharField(
        max_length=20
        )
    is_phone_verified = models.BooleanField(
        default=False
        )

class Address(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="addresses"
        )
    province = models.CharField(
        max_length=30
        ) #استان
    city = models.CharField(
        max_length=30
        )
    address = models.TextField(
        
    )
    postal_code = models.CharField(
        max_length=10
        )
