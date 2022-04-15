from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Festival(models.Model):
  ALL = 'All'
  CROATIA = 'Croatia'
  MALTA = 'Malta'

  LOCATION_CHOICES = [
        (ALL, 'All'),
        (CROATIA, 'Croatia'),
        (MALTA, 'Malta'),
    ]
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=20, choices=LOCATION_CHOICES, default=ALL)
  start_date = models.DateField(null=True)
  end_date = models.DateField(null=True)
  image = models.CharField(max_length=200, null=True)
  # attending = ManyToManyField(Attending, related_name=festival, blank=True)
  activities = ArrayField(models.CharField(max_length=30), null=True)

  def __str__(self):
      return self.name