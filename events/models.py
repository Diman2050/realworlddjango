from django.db import models
from django.core.validators import MaxValueValidator


class Event(models.Model):
    title = models.CharField(max_length=200,
                             default='',
                             verbose_name='Название'
                             )
    description = models.TextField(max_length=None,
                                   default='',
                                   verbose_name='Описание'
                                   )
    date_start = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата начала'
                                      )
    participants_number = models.SmallIntegerField(validators=[MaxValueValidator(10000)],
                                                   verbose_name='Количество участников'
                                                   )
    is_private = models.BooleanField(default=False,
                                     verbose_name='Частное'
                                     )

    class Meta:
        verbose_name_plural = 'События'
        verbose_name = 'Событие'


class Category(models.Model):
    title = models.CharField(max_length=90,
                             default='',
                             verbose_name='Категория'
                             )

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
