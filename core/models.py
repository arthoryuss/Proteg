from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from .choices import *
from django.conf import settings	
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
    UserManager)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        'Usuário', max_length=30, unique=True, validators=[username_validator],
    )
    first_name = models.CharField('first name', max_length=30)
    last_name = models.CharField('last name', max_length=30)
    email = models.EmailField('E-mail', unique=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', default=timezone.now)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.first_name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class PasswordReset(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Usuario',
        #related_name='resets',
        on_delete=models.CASCADE,
    )
    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

    def __str__(self):
        return '{0} em {1}'.format(self.user, self.created_at)

    class Meta:
        verbose_name = 'Nova Senha'
        verbose_name_plural = 'Novas Senhas'
# Create your models here.
