from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import UserProfileManager


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserProfileManager()

    # A string describing the name of the field on the user model that is used as the unique identifier
    USERNAME_FIELD = 'email'

    # A string describing the name of the email field on the User model
    EMAIL_FIELD = 'email'

    # A list of the field names that will be prompted for when creating a user via the 'createsuperuser'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        """Return string representation of the user object"""
        return self.email

    def get_full_name(self):
        """Returns the first_name plus the last_name, with a space in between"""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user"""
        return self.first_name
