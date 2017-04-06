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


    class Meta:
        model = Reservation
        fields = (
          'id', 
          'check_in_date', 
          'check_out_date', 
          'completed',
          'total', 
          'payment', 
          'room', 
          'guest')
        

    def create(self, validated_data):
        user =  self.context['request'].user
        guest= Guest.objects.get(user=user)
        room = validated_data['room']
        check_in_date=validated_data['check_in_date']
        check_out_date=validated_data['check_out_date']
        reservation=Reservation.objects.filter(check_in_date__gte=check_in_date, check_out_date__lte=check_out_date, room=room.pk)
        if len(reservation) is 0:
            return Reservation.objects.create(
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                completed=0,
                total=validated_data['total'],
                payment=validated_data['payment'],
                room=room,
                guest=guest
                )
        else:
            raise serializers.ValidationError("error")
      
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

  class Meta:
    model = Guest
    fields = (
      'id', 
      'url', 
      'user', 
      'street_address', 
      'city', 'state', 
      'zipcode' 
      )
    
class LoginSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields=('email', 'password')



