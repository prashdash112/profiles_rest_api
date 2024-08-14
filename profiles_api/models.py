from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for User profiles"""
    def create_user(self, name, email, password=None):
        """Create a new user profile"""
        if not email: 
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email=email)
        user = self.model(name=name, email=email)
        user.set_password(password)
        user.save(using = self._db)
        return user 
    
    def create_superuser(self, email,name,password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email,name,password)
        # is_superuser came from the PermissionMixin class while is_staff is created in UserProfile class
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        
        return user 


# Create your models here.
class UserProfile(AbstractBaseUser,PermissionsMixin):
    """
    Database model for Users
    """
    name  = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of a User"""
        return self.name
    
    def get_shot_name(self):
        """ Retrieve shot name of a User"""

    def __str__(self):
        """Returns a string representation of the object when printed"""
        return self.email