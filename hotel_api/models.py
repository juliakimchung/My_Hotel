from django.db import models


# Create your models here.
class Room(models.Model):
    """
        Class to create a table representing a room
        extension of models.Model
        Variables:
            
            name: the name of the room
            description: description on the room type and detailed info on the room 
            amenity: amenity type and descriptions on it per room
            price: price per room
            availability: whether the room is already booked or occupied, availability status
            
    """

    
    name = models.CharField(max_length = 200, blank=True, default="")
    description = models.TextField()
    amenity = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    availability = models.Boolean(default=False)

class PaymentType(models.Model):
    name = models.CharField(max_length = 200, blank=True, default="")
    account_number = models.CharField(max_length= 100, blank = True )

class Reservation(models.Model):
    date = models.DateTimeField()
    room = models.ForeignKey("Room", related_name="reservations", delete_on=modeles.CASCADE)
    payment_type = models.ForeignKey('PaymentType', related_name="reservations", delete_on=models.CASCADE)



