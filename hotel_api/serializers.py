from rest_framework import serializers
from hotel_api.models import *
from django.contrib.auth.models import User
from django.contrib.auth import models

class ReservationSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Reservation
		fields = ('id', 'url', 'check_in_date', 'check_out_date', 'completed', 'payment_type', 'room', 'guest')

class RoomSerializer(serializers.HyperlinkedModelSerializer):


	class Meta:
		model = Room
		fields = ('id', 'url', 'name', 'availability', 'price', 'description', 'amenity', 'size' )

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = PaymentType 
		fields = ('id', 'url', 'name', 'account_number', 'ccv_number', 'expiration_date')