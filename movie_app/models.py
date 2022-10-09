from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    duration = models.IntegerField()
    director = models.ForeignKey(
        to=Director,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='movie',
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(
        to=Movie,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='review',
    )