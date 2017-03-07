from rest_framework import serializers
from hotel_api.models import *
from django.contrib.auth.models import User
from django.comtrib.auth import models

class ReservationSerializer(serializer.HyperlinkedModelSerializer):

	class Meta:
		model = Reservation
		fields = ('id', 'url', 'date', 'active', 'payment_type', 'room', 'guest')

class RoomSerializer(serializer.HyperlinkedModelSerializer):


	class Meta:
		model = Room
		fields = ('id', 'url', 'name', 'availability', 'price', 'description', 'amenity' )

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = PaymentType 
		fields = ('id', 'url', 'name', 'account_number', 'cvv', 'expiration_date', 'guest')