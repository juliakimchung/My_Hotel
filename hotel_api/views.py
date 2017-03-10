from django.shortcuts import render
from hotel_api.models import *
from hotel_api.serializers import *
from rest_framework import generics
from rest_framework import reverse
from rest_framework.response import Response 
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate 
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
class GuestViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = GuestSerializer

class ReservationViewSet(viewsets.ModelViewSet):

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class PaymentTypeViewSet(viewsets.ModelViewSet):

    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer

class RoomViewSet(viewsets.ModelViewSet):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
















