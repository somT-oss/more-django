"""
Imports uuid4 for updating default primary_key value for models
"""
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """
    Custom user model manager that handles creating buyers and sellers for the backend
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Function that handles creating user.
        @params email: user email | null=False
        @params password: user password | null=False
        """
        if not email:
            raise ValueError('Enter your email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Function that handles creating superuser.
        @params email: superuser email | null=False
        @params password: superuser password | null=False
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff attr set to True')

        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser attr set to True')

        user = self.create_user(email, password, **extra_fields)
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user class with attributes
    """
    class Hostels(models.TextChoices):
        """
        Choices for available hostels
        """
        BIOBAKU = "1", "Prof. Saburi Biobaku Hall"
        ENI_NJOKU = "2", "Prof. Eni Njoku Hall"
        MARIERE = "3", "Baluba Kingdom"
        JAJA = "4", "King Jaja Hall"
    id = models.CharField(default=uuid.uuid4, primary_key=True)
    first_name = models.CharField(max_length=50,
                                  blank=False,
                                  null=False,
                                  help_text="User first name")
    last_name = models.CharField(max_length=50, blank=False,
                                 null=False,
                                 help_text="User last name")
    email = models.EmailField(null=False,
                              blank=False,
                              unique=True,
                              help_text="User email")
    hostel = models.CharField(null=False,
                              blank=False,
                              choices=Hostels,
                              help_text="User's hostel")
    room_name = models.CharField(max_length=30,
                                 blank=False,
                                 null=False,
                                 help_text="User's room name")
    is_seller = models.BooleanField(default=False,
                                    null=False,
                                    blank=False,
                                    help_text="Check if user is a seller")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self) -> str:
        return f"{(self.first_name + self.last_name).upper()}"
