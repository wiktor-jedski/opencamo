from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True, unique=True)
    address = models.TextField()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.alias is None:
            self.alias = self.name
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.alias


class Airport(Location):
    IATA_code = models.CharField(max_length=3, unique=True)


class Unit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
