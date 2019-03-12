from django.db import models

# Create your models here.
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)


