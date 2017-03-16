from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import Decimal


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

    image = models.FileField(max_length=None)
    name = models.CharField(max_length = 200, blank=True, default="")
    size = models.CharField(max_length = 100, blank =True)
    description = models.TextField(max_length=1400, default="")
    amenity = models.TextField(max_length=1500, default="")
    price = models.DecimalField(max_digits=20, decimal_places=2)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Rooms'

class PaymentType(models.Model):
    name = models.CharField(max_length = 100)
    account_number = models.CharField(max_length= 16, unique= True )
    ccv_number = models.CharField(max_length=3)
    expiration_date = models.CharField(max_length=10)

    def __str__(self):
        return '{}{}'.format(self.name, self.account_number)

    class Meta:
        verbose_name_plural = 'PaymentTypes'


class Reservation(models.Model):
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    completed = models.IntegerField(default = 0)
    total = models.DecimalField(max_digits=10, decimal_places=2 , default=Decimal(0))
    room = models.ForeignKey("Room", related_name="reservations", on_delete=models.CASCADE)
    guest = models.ForeignKey('Guest', related_name='reservations', on_delete=models.CASCADE)
    payment = models.ForeignKey('PaymentType', related_name="reservations", on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.completed)

    class Meta:
        verbose_name_plural = "Reservations"


class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return "{}".format(self.user)






