from django.db import models
from bson import ObjectId

class User(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()))
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Team(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()))
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(User, related_name='teams')

class Activity(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration = models.DurationField()

class Leaderboard(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.IntegerField()

class Workout(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()))
    name = models.CharField(max_length=100)
    description = models.TextField()
