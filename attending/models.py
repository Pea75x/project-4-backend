from django.db import models
from festivals.models import Festival
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField

user = get_user_model()


# Create your models here.
class Attending(models.Model):
  festival = models.ForeignKey(Festival, related_name='attending', on_delete=models.CASCADE)
  user = models.ForeignKey(user, related_name='attending', on_delete=models.CASCADE)
  arrival_date = models.DateField()
  depart_date = models.DateField()
  price_min = models.FloatField(null=True)
  price_max = models.FloatField(null=True)
  activities = ArrayField(models.CharField(max_length=30), null=True)
  comment = models.TextField(max_length=400)
  def __str__(self):
    return f'{self.festival} - {self.user}'