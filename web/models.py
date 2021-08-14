from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    passed_test = models.BooleanField(default=False)
    test_result = models.CharField(max_length=100, null=True, blank=True)


class Course(models.Model):
    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    is_active = models.BooleanField(default=False, verbose_name='Показывать')
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    photo = models.ImageField(null=True, blank=True, verbose_name='Фото')
    preview = models.FileField(null=True, blank=True, verbose_name='Видео превью')

    price = models.DecimalField(max_digits=8, decimal_places=0, verbose_name='Цена', null=True, blank=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    class Meta:
        verbose_name = 'занятие'
        verbose_name_plural = 'заняния'

    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Курс')

    number = models.PositiveIntegerField(null=True, blank=True, verbose_name='Номер')
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    video = models.FileField(null=True, blank=True, verbose_name='Видео')
    materials = models.FileField(null=True, blank=True, verbose_name='Материалы')

    def __str__(self):
        return f'Занятие №{self.number}. {self.title}'
