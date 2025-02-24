from django.db import models

# Create your models here.

class Weather(models.Model):
    city = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.city} - {self.temperature}°C'
