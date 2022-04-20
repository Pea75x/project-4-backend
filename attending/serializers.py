from rest_framework import serializers
from .models import Attending
from jwt_auth.serializers import PublicUserSerializer
from festivals.serializers.common import FestivalSerializer

class AttendingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Attending
    fields = ('__all__')

class PopulatedAttendingSerializer(AttendingSerializer):
  user = PublicUserSerializer()

