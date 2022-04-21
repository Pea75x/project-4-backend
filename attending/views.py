from django.shortcuts import render
from .models import Attending
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AttendingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class AttendingPost(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
      request.data['user'] = request.user.id
      attending_serializer = AttendingSerializer(data= request.data)
      if attending_serializer.is_valid():
        attending_serializer.save()
        return Response(data = attending_serializer.data, status = status.HTTP_201_CREATED)
      return Response (data= attending_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

