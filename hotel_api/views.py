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
import django_filters

class GuestViewSet(viewsets.ModelViewSet):

    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.user_is_superuser:
            return RestrictedUserSerializer
        return UserSerializer

class ReservationViewSet(viewsets.ModelViewSet):


    serializer_class = ReservationSerializer

    def get_queryset(self):
        current_reservation = Reservation.objects.filter(guest__user=self.request.user)
        
       
        return current_reservation





class PaymentTypeViewSet(viewsets.ModelViewSet):

    queryset = PaymentType.objects.all()    
    serializer_class = PaymentTypeSerializer


    
class RoomViewSet(viewsets.ModelViewSet):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    

class RegisterView(generics.RetrieveAPIView):
    """
    """
    
    permission_classes = (AllowAny,)

    error_messages = {
        'invalid': "Invalid username or password",
        'disabled': "Sorry, this account is suspended",
    }

    def _error_response(self, message_key):
        data = json.dumps({
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        })

    @csrf_exempt
    def post(self,request):
        permission_classes = (AllowAny,)

        req_body = json.loads(request.body.decode())
        print(req_body)

        user = User.objects.create_user(
            username = req_body['username'],
            password = req_body['password'],
            email = req_body['email'],
            first_name = req_body['first_name'],
            last_name = req_body['last_name']
            )
        guest = Guest.objects.create(
            user = user,
            street_address = req_body['street_address'],
            city = req_body['city'],
            zipcode = req_body['zipcode'],
            state = req_body['state'])
        
        return HttpResponse({"status": True})











