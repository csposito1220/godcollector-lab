from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

PRAYERS = (
    ('P', 'Prosperity'),
    ('F', 'Food'),
    ('S', 'Safety'),
)

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
    
    def prayed_for_today(self):
        return self.prayer_set.filter(date=date.today()).count() >= len(PRAYERS)

class Prayer(models.Model):
    date = models.DateField('Prayer Date')
    prayer = models.CharField(
        max_length=1,
        choices=PRAYERS,
        default=PRAYERS[0][0]
    )

    mythology = models.ForeignKey(
        Mythology,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_prayer_display()} on {self.date}"

    class Meta:
        ordering = ['-date']