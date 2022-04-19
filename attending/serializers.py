from rest_framework import serializers
from .models import Attending
from jwt_auth.serializers import PublicUserSerializer

class AttendingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Attending
    fields = ('__all__')

class PopulatedAttendingSerializer(AttendingSerializer):
  user = PublicUserSerializer()