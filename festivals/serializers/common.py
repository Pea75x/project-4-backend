from rest_framework import serializers
from ..models import *
from jwt_auth.serializers import *
# from attending.serializers import PopulatedAttendingSerializer

class FestivalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Festival
    fields = ("__all__")

class HotelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hotel
    fields = ('__all__')

#! To use for festival page, shows hotel and user details
class PopulatedFestivalSerializer(FestivalSerializer):
  hotel = HotelSerializer(many=True)
  # attending = PopulatedAttendingSerializer(many=True)

class PopulatedHotelSerializer(HotelSerializer):
  festival = FestivalSerializer()


class MessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Message
    fields = ('__all__')

# class GroupTripSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Message
#     fields = ('__all__')

# class PopulatedGroupTripSerializer(GroupTripSerializer):
#   members = UserSerializer(many=True)
#   pending_members = UserSerializer(many=True)

