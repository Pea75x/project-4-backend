from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
#from festivals.models import Festival
# Create your models here.

class CustomUser(AbstractUser):
  image = models.CharField(max_length=200)
  pending_friends = ArrayField(models.CharField(max_length=30), null=True)
  friends = ArrayField(models.CharField(max_length=30), null=True)
  pending_trips = ArrayField(models.CharField(max_length=30), null=True)
  trips = ArrayField(models.CharField(max_length=30), null=True)

