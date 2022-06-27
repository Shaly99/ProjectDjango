from tkinter import CASCADE
from turtle import title
from django.db import models

# Create your models here.
class Serie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

class Episode(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)