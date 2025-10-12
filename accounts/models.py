from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.pop('role', None) # Impede qualquer tentativo de definir um role
        if not email:
            raise ValueError("Email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', User.Roles.ADMIN)
        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser precisa ter is_staff=True.')
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrador'
        STAFF = 'STAFF', 'Funcionário'
        CLIENT = 'CLIENT', 'Cliente'

    email = models.EmailField('e-mail', unique=True)
    first_name = models.CharField('nome', max_length=150)
    last_name = models.CharField('sobrenome', max_length=150, blank=True)
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)
    telefone = models.CharField('telefone', max_length=20, blank=True)
    role = models.CharField('perfil', max_length=10, choices=Roles.choices, default=Roles.CLIENT)

    is_staff = models.BooleanField('é staff', default=False)
    is_active = models.BooleanField('ativo', default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.email