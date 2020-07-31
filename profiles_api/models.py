from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ manager to communicate with python cli using cutomize model """

    def create_user(self,email,name,password):
        if not email:
            raise ValueError("user must have an email address")

        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,email,name,password):
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self.db)
        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Customize model for database """
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """ Function to get the full name """
        return self.name

    def get_short_name(self):
        """ Function to get the short name """
        return self.name

    def __str__(self):
        """ Function to get email """
        return self.email


# Create your models here.