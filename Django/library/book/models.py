from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    def __str__(self):
        return f'{str(self.name).upper()[0]} {self.surname}'

class Genre(models.Model):
    genre = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.genre}'

class Plot(models.Model):
    plot = models.TextField()
    def __str__(self):
        return f'{str(self.plot).upper()[:15]}'

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    priсe = models.FloatField()
    page_count = models.IntegerField()
    description = models.TextField()
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(to=Genre)
    plot = models.OneToOneField(to=Plot, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.priсe}BY'
