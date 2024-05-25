from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)

        return user



class User(AbstractBaseUser, PermissionsMixin):
    
    first_name = models.CharField(max_length=128, verbose_name="nombres",null=True )
    last_name = models.CharField(max_length=128, verbose_name="apellidos",null=True )
    company = models.CharField(max_length=128, verbose_name="start up/empresa",null=True )
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, verbose_name="password", null=True)
    total_registros = models.PositiveBigIntegerField(default=0)
    date_joined = models.DateTimeField(default=timezone.now)
    is_paid = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


