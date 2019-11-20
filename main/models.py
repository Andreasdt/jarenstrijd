from django.db import models


class Jaar(models.Model):
    jaar_naam = models.CharField(max_length=50, primary_key=True)
    aantal_punten = models.IntegerField(default=0)
    jaar = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Jaren'

    def __str__(self):
        return self.jaar_naam
