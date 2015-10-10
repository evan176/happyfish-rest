from django.db import models

# Create your models here.

class Aquarium(models.Model):
    updated_time = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    ph = models.FloatField()

    class Meta:
        ordering = ('updated_time',)
