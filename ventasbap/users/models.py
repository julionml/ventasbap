from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()


class CompleteUser(CustomUser):
    City = models.CharField(max_length=30)
    Bdate =  models.DateField()
    sex = models.CharField(max_length=30)
    Id = models.IntegerField()
    cellphone = models.IntegerField()
