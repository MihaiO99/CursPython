from django.db import models


# Create your models here.

class Location(models.Model):  # pentru a modela tabelul Location

    objects = None
    city = models.CharField(max_length=100)  # varchar in baza de date
    country = models.CharField(max_length=100)
    active = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.city} {self.country}"