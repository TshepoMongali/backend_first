from django.db import models

# Create your models here.
class Tour(models.Model):
    # origin country
    origin_country = models.CharField(max_length=64)
    # destination
    destination_country = models.CharField(max_length=64)
    # number of nights
    number_of_nights = models.IntegerField()
    
    # prices for the tour
    
    price = models.IntegerField()
    
    #string epresentation of tours
    
    def __str__(self):
        return (f"ID:{self.id}: From {self.origin_country} To {self.destination_country},{self.number_of_nights}  nights costs $ {self.price}")