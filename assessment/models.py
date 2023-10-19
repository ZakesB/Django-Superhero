from django.db import models


class SuperHero(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    alignment = models.CharField(max_length=10, blank=False, null=False)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
