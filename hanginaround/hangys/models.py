from django.db import models

# Create your models here.
class Tour(models.Model):
    origin_country = models.CharField(max_length= 64)
    destination_country = models.CharField(max_length = 64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    #String representaion
    def __str__(self):
        return (f"ID: {self.id}: From: {self.origin_country} To:"
                f"{self.destination_country}, {self.number_of_nights} "
                f"nights costs ${self.price}")