from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager


# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        'Никнейм', max_length=64, unique=True, null=True, blank=True
    )
    email = models.EmailField('Почта', unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username} ({self.email})'