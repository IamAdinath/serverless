from django.db import models

# Create your models here.


class Sensors(models.Model):
    id = models.BigAutoField()
    device = models.CharField(max_length=150)
    name = models.CharField(max_length=120)
    sensor = models.CharField(max_length=350)

    def __str__(self):
        return self.device
