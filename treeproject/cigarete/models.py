from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your models here.

class Cigarete(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name