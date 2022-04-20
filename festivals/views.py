from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import * 
from .serializers.common import * 

#! FESTIVALS
# GET ALL FESTIVALS/ CREATE FESTIVAL
class FestivalList(ListCreateAPIView):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer

# GET FESTIVAL BY ID
class FestivalById(RetrieveAPIView):
  queryset = Festival.objects.all()
  serializer_class = PopulatedFestivalSerializer

# UPDATE OR DELETE FESTIVAL
class FestivalUpdateDestroy(RetrieveUpdateDestroyAPIView):
  queryset = Festival.objects.all()
  serializer_class = FestivalSerializer

#!HOTEL
# GET ALL HOTELS/ CREATE HOTEL
class HotelList(ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

# GET HOTEL BY ID
class HotelById(RetrieveAPIView):
  queryset = Hotel.objects.all()
  serializer_class = PopulatedHotelSerializer

# UPDATE OR DELETE HOTEL
class HotelUpdateDestroy(RetrieveUpdateDestroyAPIView):
  queryset = Hotel.objects.all()
  serializer_class = HotelSerializer


# class MessageList(ListCreateAPIView):
#   quer

