from django.shortcuts import render
from .serializers.common import FestivalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *



# Create your views here.
class FestivalList(APIView):
  def get(self, request):
    serializer = FestivalSerializer(festival, many=True)
    return Response(serializer.data)