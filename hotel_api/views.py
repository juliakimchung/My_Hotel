from django.shortcuts import render
from hotel_api.models import *
from hotel_api.serializers import *
from rest_framework import generics
from rest_framework import reverse
from rest_framework.response import Response 
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework import permissions
from django.contrib.auth.models import User

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):

	queryset = User.objects.all()

class ReservationViewSet(viewsets.ModelViewSet):

	queryset = Reservation.objects.all()
	serializer_class = ReservationSerializer

class PaymentTypeViewSet(viewsets.ModelViewSet):

	queryset = PaymentType.objects.all()
	serializer_class = PaymentTypeSerializer

class RoomViewSet(viewsets.ModelViewSet):

	queryset = Room.objects.all()
	serializer_class = RoomSerializer

