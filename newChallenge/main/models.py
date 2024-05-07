# -*- encoding: utf-8 -*-
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _



# Create your models here.
class CustomUserManager(BaseUserManager):
    """
    Custom user manager where the username field is replaced with the email field.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    email = models.EmailField(blank=False, null=False, unique=True)
    password = models.CharField(max_length=100, blank=False, null=False)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_authorized = models.BooleanField(default=False, blank=True, null=True)
    last_login = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_ts =  models.DateTimeField(auto_now_add=True, blank=False, null=False)   
    is_staff = models.BooleanField(default=False, blank=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True, null=True)

    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = 'User'

    def __str__(self):
        return self.email
    

class Ads(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    created_ts =  models.DateTimeField(auto_now_add=True, blank=False, null=False)   
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Ads'

    def __str__(self):
        return self.user.email + '_' + self.title
    

class Comments(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=False, null=False)
    ad = models.ForeignKey(to=Ads, on_delete=models.CASCADE, blank=False, null=False)
    comment = models.ForeignKey(to='self', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(blank=False, null=False)
    created_ts =  models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.user.email}_{self.ad.title}_{self.pk}'
      

