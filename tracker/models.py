from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()
    notes = models.TextField(blank=True, null=True)

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, related_name='exercises', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    repetitions = models.IntegerField()
    sets = models.IntegerField()

class Nutrition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    calories = models.IntegerField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()
    body_fat_percentage = models.FloatField()

