from django.db import models
from django.contrib.auth import get_user_model
from users.models import User


class Task(models.Model):
    name = models.CharField('Название', max_length=255, )
    description = models.TextField('Описание', null=True, blank=True, )
    status = models.BooleanField('Завершена', default=False, )
    created = models.DateField('Время создания', auto_now_add=True)
    due_to = models.DateField('Дедлайн', null=True, blank=True, )
    owner = models.ForeignKey(
        User, models.CASCADE, 'tasks', verbose_name='Задача', 
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ('-created', 'name')
    
    def __str__(self):
        return f"{self.name}({self.status})"