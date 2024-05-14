"""Docstring."""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Опишите модель Contest здесь!
class Contest(models.Model):
    """Docstring."""

    title = models.CharField(verbose_name="Название", max_length=20)
    description = models.TextField(verbose_name="Описание")
    price = models.IntegerField(
        verbose_name='Цена',
        help_text='Рекомендованная розничная цена',
        validators=[MaxValueValidator(100), MinValueValidator(10)]
    )
    comment = models.TextField(verbose_name="Комментарий", blank=True)
