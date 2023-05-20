"""Users model file."""

import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser
)


GENDER_CHOICES = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ('OTHER', 'OTHER'),
)


class UserManager(BaseUserManager):
    """User manager class."""

    def create_user(self, email, password = None, **extrafields):
        """Create a normal user."""
        if not email:
            raise ValueError(_("Email address is required"))
        
        user = self.model(email=self.normalize_email(email), **extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password = None, **fields):
        """Create a superuser."""
        user = self.create_user(email, password=password, first_name=first_name, last_name=last_name, **fields)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user    


class User(AbstractBaseUser):
    """User model class."""

    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True, auto_created=True)
    created_on = models.DateTimeField(
        db_index=True, editable=False, default=timezone.now)    
    updated_on = models.DateTimeField(db_index=True, default=timezone.now)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    first_name = models.CharField(max_length=300, null=False, blank=False)
    last_name = models.CharField(max_length=300, null=False, blank=False)
    other_names = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField(max_length=300, null=False, blank=False, unique=True, verbose_name='email address')
    password = models.CharField(max_length=300, null=True, blank=True)
    phone_number = models.CharField(max_length=300, null=True, blank=True)
    date_of_birth =  models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=300, choices=GENDER_CHOICES, null=False, blank=False)
    join_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
   
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
