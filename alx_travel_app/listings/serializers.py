"""This module sets up serializers for Listing and Booking Models"""

from rest_framework import serializers

from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    """Listing serializer"""

    class Meta:
        model = Listing
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["host"] = instance.host
        representation["property"] = instance.property
        return representation


class BookingSerializer(serializers.ModelSerializer):
    """Booking serializer"""

    class Meta:
        model = Booking
        fields = "__all__"
    

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["guest"] = instance.guest
        representation["property"] = instance.property
        return representation