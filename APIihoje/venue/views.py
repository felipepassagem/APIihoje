from django.shortcuts import render
from .permissions import IsOwnerOrAdmin

# Create your views here.
from rest_framework import generics
from .models import Venue
from .serializers import VenueSerializer

class VenueList(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class VenueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class CreateVenue(generics.CreateAPIView):
    serializer_class = VenueSerializer

class UpdateVenue(generics.UpdateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class CreateVenue(generics.CreateAPIView):
    permission_classes = [IsOwnerOrAdmin]  # Apenas owners e admins podem criar venues
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class UpdateVenue(generics.UpdateAPIView):
    permission_classes = [IsOwnerOrAdmin]  # Apenas owners e admins podem atualizar venues
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class DeleteVenue(generics.DestroyAPIView):
    queryset = Venue.objects.all()