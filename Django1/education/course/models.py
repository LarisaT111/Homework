from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    duration = models.TextField(verbose_name='Длительность')
    description = models.TextField(verbose_name='Описание')


    def __str__(self):
        return f'#{self.pk} - {self.title}'
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курс'

class Topic(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'#{self.pk} - {self.name}'
    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


