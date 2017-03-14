from rest_framework import serializers
from hotel_api.models import *
from django.contrib.auth.models import User
from django.contrib.auth import models
from django.forms.fields import FileField

class PaymentTypeSerializer(serializers.ModelSerializer):

  class Meta:
    model = PaymentType 
    fields = (
      'id', 
      'name', 
      'account_number',
      'ccv_number', 
      'expiration_date')

class ReservationSerializer(serializers.ModelSerializer):
    # payment= PaymentTypeSerializer(many=False)
    class Meta:
        model = Reservation
        fields = (
          'id', 
          'check_in_date', 
          'check_out_date', 
          'completed', 
          'payment', 
          'room', 
          'guest')
        

    def create(self, validated_data):
        user =  self.context['request'].user
        guest= Guest.objects.get(user=user)

        return Reservation.objects.create(
            check_in_date=validated_data['check_in_date'],
            check_out_date=validated_data['check_out_date'],
            completed=0,
            payment=validated_data['payment'],
            room=validated_data['room'],
            guest=guest
            )
      
class RoomSerializer(serializers.HyperlinkedModelSerializer):


  class Meta:
    model = Room
    fields = (
      'id',
      'url', 
      'name', 
      'availability', 
      'price', 
      'description', 
      'amenity', 
      'size', 
      'image')


class UserSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = User
    fields = (
      'id', 
      'url', 
      'username', 
      'email')

class RestrictedUserSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = User
    fields = (
      'id', 
      'first_name', 
      'last_name')

class RestrictedGuestSerializser(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Guest
    fields = (
      'id',
      'url',
      'first_name',
      'last_name',)



class GuestSerializer(serializers.ModelSerializer):
  """
  Class for data serialization of a specific Model: User
  If user is not staff, This UserSerializer will be picked up on the viewset
  """

  reservation = serializers.HyperlinkedRelatedField(many=True, view_name="reservation_detail", read_only='true')
  class Meta:
    model = Guest
    fields = (
      'id', 
      'url', 
      'user', 
      'street_address', 
      'city', 'state', 
      'zip_code', 
      'reservation')
    
class LoginSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields=('email', 'password')



