from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class AccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an Email address')
        if not first_name:
            raise ValueError('Users must have a First name')
        if not last_name:
            raise ValueError('Users must have a Last name')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_active=True
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.role = 'admin'
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, )
    last_name = models.CharField(max_length=30, )
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    is_admin = models.BooleanField(default=False)  # a superuser
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    is_superuser = models.BooleanField(default=False)
    role = models.CharField(max_length=10)
    phone = models.CharField(max_length=17, unique=True, blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Email & Password are required by default.

    objects = AccountManager()

    def __str__(self):  # __unicode__ on Python 2
        return self.first_name + ' ' + self.last_name

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class BaseModels(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class UnitOfHistory(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name="Name of Content",
        help_text="The name of the content from which this unit of history is generated"
    )
    description = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name="Description of Content",
        help_text="From where this unit of history is generated"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="history"
    )
    # Generic Foreignkey Configuration. DO NOT CHANGE
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

