"""
Imports uuid4 for updating default primary_key value for models
"""
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django_resized import ResizedImageField


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
        BIOBAKU = "biobaku", "Prof. Saburi Biobaku Hall"
        ENI_NJOKU = "eni_njoku", "Prof. Eni Njoku Hall"
        MARIERE = "mariere", "Baluba Kingdom"
        JAJA = "jaja", "King Jaja Hall"
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
    is_staff = models.BooleanField(default=False,
                                   help_text='Staff user')
    is_seller = models.BooleanField(default=False,
                                    null=False,
                                    blank=False,
                                    help_text="Check if user is a seller")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        """
        Meta class for handling model functionality
        """
        verbose_name = "USER"
        verbose_name_plural = "USERS"

    def __str__(self) -> str:
        return f"{(self.first_name + self.last_name).upper()}"


class BusinessOwnerProfile(models.Model):
    """
    Model that represents a sellers Profile
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    profile_picture = ResizedImageField(size=[400, 400], upload_to='profile_picture', default='profile_pic/default.png')
    business_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text="User business name"
    )
    business_description = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text="User business description"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        null=False,
        blank=False,
        help_text="Date business profile was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date business profile was edited"
    )

    class Meta:
        """
        Meta class for overriding default model functionality
        """
        ordering = '-created_at',
        verbose_name = 'BUSINESS_PROFILE'
        verbose_name_plural = 'BUSINESS_PROFILES'

    def __str__(self):
        return self.business_name


class BuyerProfile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text="Profile for buyers"
    )
    profile_picture = ResizedImageField(size=[400, 400], upload_to='profile_picture', default='profile_pic/default.png')
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        null=False,
        blank=False,
        help_text="Date buyer profile was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date buyer profile was edited"
    )

    class Meta:
        """
        Meta class for overriding default model functionality
        """
        ordering = '-created_at',
        verbose_name = 'BUYER_PROFILE'
        verbose_name_plural = 'BUYER_PROFILE'

    def __str__(self):
        return self.user.name

class Community(models.Model):
    """
    Model that represents a community
    """
    id = models.CharField(default=uuid.uuid4, primary_key=True)
    community_owner = models.ForeignKey(CustomUser,
                                        on_delete=models.CASCADE,
                                        help_text="Owner of the community")
    name = models.CharField(max_length=50,
                            null=False,
                            blank=False,
                            help_text="Community name")
    description = models.TextField(max_length=250,
                                   null=False,
                                   blank=False,
                                   help_text="Community description")
    community_members = models.ManyToManyField(CustomUser,
                                               related_name="members")
    created_at = models.DateTimeField(auto_now_add=True,
                                      editable=False,
                                      help_text="Date the community was create")

    class Meta:
        """
        Meta class for overriding default model behaviours
        """
        verbose_name = 'COMMUNITY'
        verbose_name_plural = 'COMMUNITIES'

    def __str__(self) -> str:
        return self.name
