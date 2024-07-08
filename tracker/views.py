from django.shortcuts import render, get_object_or_404
from .models import Workout, Exercise, Nutrition, Progress

def dashboard(request):
    workouts = Workout.objects.filter(user=request.user)
    nutrition = Nutrition.objects.filter(user=request.user)
    progress = Progress.objects.filter(user=request.user)
    context = {
        'workouts': workouts,
        'nutrition': nutrition,
        'progress': progress,
    }
    return render(request, 'tracker/dashboard.html', context)

def add_workout(request):
    # Logic for adding a workout
    pass

def add_nutrition(request):
    # Logic for adding nutrition
    pass

def add_progress(request):
    # Logic for adding progress
    pass









# git push -f origin main

