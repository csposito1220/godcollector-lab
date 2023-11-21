from django.db import models
from django.urls import reverse

# Create your models here.

class God(models.Model):
    name = models.CharField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'God_id': self.id})

class Mythology(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    gods = models.ManyToManyField(God)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('mythologies_detail', kwargs={'pk': self.id})
