from rest_framework import serializers
from hotel_api.models import *
from django.contrib.auth.models import User
from django.contrib.auth import models
from django.forms.fields import ImageField

class ReservationSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Reservation
		fields = ('id', 'url', 'check_in_date', 'check_out_date', 'completed', 'payment_type', 'room', 'guest')
		depth = 1

class RoomSerializer(serializers.HyperlinkedModelSerializer):


	class Meta:
		model = Room
		fields = ('id', 'url', 'name', 'availability', 'price', 'description', 'amenity', 'size', 'image')

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = PaymentType 
		fields = ('id', 'url', 'name', 'account_number', 'ccv_number', 'expiration_date')

class GuestSerializer(serializers.ModelSerializer):
	"""
	Class for data serialization of a specific Model: User
	If user is not staff, This UserSerializer will be picked up on the viewset
	"""
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')
		extra_kwargs = {'email': {'write_only': True}, 'username': {'write_only': True}}
		depth = 0

class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('email', 'password')



