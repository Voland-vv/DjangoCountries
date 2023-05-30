from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=64)


class Country(models.Model):
    name = models.CharField(max_length=128)
    languages = models.ManyToManyField(to=Language)