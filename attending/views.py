from django.shortcuts import render
from .models import Attending
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from .serializers import AttendingSerializer

# Create your views here.
class AttendingPost(ListCreateAPIView):
    queryset = Attending.objects.all()
    serializer_class = AttendingSerializer