from django.db import models
from django.contrib.auth.models import User


class Crew(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class AirplaneType(models.Model):
    name = models.CharField(max_length=100)


class Order(models.Model):
    crated_at = models.DateTimeField(auto_now_add=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)


class Airport(models.Model):
    name = models.CharField(max_length=100)
    closest_big_city = models.CharField(max_length=100)
