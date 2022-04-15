from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
# from rest_framework.views import APIView 
# from rest_framework.response import Response 
from .models import * 
from .serializers.common import * 


# Create your views here.
class FestivalList(ListCreateAPIView):
    queryset = Festival.objects.all()
    serializer_class = PopulatedFestivalSerializer

