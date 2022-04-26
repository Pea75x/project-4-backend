from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from jwt_auth.models import CustomUser

# Create your models here.
class Festival(models.Model):
  ALL = 'All'
  CROATIA = 'Croatia'
  FRANCE = 'France'
  GERMANY = 'Germany'
  HUNGARY = 'Hungary'
  MALTA = 'Malta'
  MEXICO = 'Mexico'
  NETHERLANDS = 'Netherlands'
  SPAIN = 'Spain'
  AMERICA = 'USA'
  BELGIUM = 'Belgium'
  
  LOCATION_CHOICES = [
        (ALL, 'All'),
        (CROATIA, 'Croatia'),
        (FRANCE, 'France'),
        (GERMANY, 'Germany'),
        (HUNGARY, 'Hungary'),
        (MALTA, 'Malta'),
        (MEXICO, 'Mexico'),
        (NETHERLANDS, "Netherlands"),
        (SPAIN, 'Spain'),
        (AMERICA, 'USA'),
        (BELGIUM, 'Belgium')
    ]
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=20, choices=LOCATION_CHOICES, default=ALL)
  start_date = models.DateField(null=True)
  end_date = models.DateField(null=True)
  image = models.CharField(max_length=200, null=True)
  activities = ArrayField(models.CharField(max_length=50), null=True)
  lat = models.FloatField(null=True)
  long = models.FloatField(null=True)

  def __str__(self):
      return self.name

class Hotel(models.Model):
  name = models.CharField(max_length=50)
  image = models.CharField(max_length=200, null=True)
  rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
  festival = models.ForeignKey(Festival, related_name='hotel', on_delete=models.CASCADE, blank=True, null=True)
  lat = models.FloatField(null=True)
  long = models.FloatField(null=True)
  website = models.CharField(max_length=200, null=True)
  def __str__(self):
    return self.name

class Message(models.Model):
  source_user = models.ForeignKey(CustomUser, related_name='source_user_message', on_delete=models.CASCADE)
  destination_user = models.ForeignKey(CustomUser, related_name='destination_user_message', on_delete=models.CASCADE)
  text = models.CharField(max_length=500)
  created_date = models.DateTimeField(auto_now_add = True)

  def __str__(self):
      return f'{self.source_user} to {self.destination_user}'

class GroupTrip(models.Model):
  pending_members = ArrayField(models.CharField(max_length=20), null=True)
  members = ArrayField(models.CharField(max_length=20), null=True)
  Festival = models.ForeignKey(Festival, related_name="group_trip", on_delete=models.CASCADE, null=True)
  hotel = models.ForeignKey(Hotel, related_name='group_trip', on_delete=models.CASCADE, null=True)

