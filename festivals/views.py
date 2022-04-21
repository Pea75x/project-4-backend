from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .models import * 
from .serializers.common import * 
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, filters
from rest_framework.response import Response

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

#! MESSAGES
# send message
class SendMessage(APIView):
  permission_classes = [IsAuthenticated,]

  def post(self, request):
    request.data['source_user'] = request.user.id
    message_serializer = MessageSerializer(data= request.data)
    if message_serializer.is_valid():
      message_serializer.save()
      return Response(data = message_serializer.data, status= status.HTTP_201_CREATED)
    return Response (data= message_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class getAllMessages(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class getFriendsMessages(ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
      queryset = Message.objects.all()
      destinationUserId = int(self.request.query_params.get('destinationUserId'))
      print(self.request.user.id)
      sourceUserId = self.request.user.id

      if destinationUserId:
        sent_messages = queryset.filter(destination_user=destinationUserId, source_user=sourceUserId)
      received_messages = queryset.filter(destination_user=sourceUserId, source_user=destinationUserId)
      all_messages = list(sent_messages) + list(received_messages)
      return all_messages