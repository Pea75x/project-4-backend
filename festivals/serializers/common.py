from rest_framework import serializers
from ..models import *
from jwt_auth.serializers import *

class FestivalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Festival
    fields = ("__all__")

class HotelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hotel
    fields = ('__all__')

class AttendingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Attending
    fields = ('__all__')

class AttendingWithUserSerializer(AttendingSerializer):
  user = PublicUserSerializer()

class PopulatedFestivalSerializer(FestivalSerializer):
  hotel = HotelSerializer(many=True)
  attending = AttendingWithUserSerializer(many=True)
