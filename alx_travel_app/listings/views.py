from django.shortcuts import render
from rest_framework import viewsets
from .models import Booking, Listing
from .serializers import BookingSerializer, ListingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
