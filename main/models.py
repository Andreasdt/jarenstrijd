from django.db import models

class Jaar(models.Model):
    jaar_naam = models.CharField(max_length=50)
    aantal_punten = models.IntegerField()
