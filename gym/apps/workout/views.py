from django.shortcuts import render
from django.http import HttpResponse

from .models import Workout, WorkoutPlan


def index(request):
    return HttpResponse("Workout's urls works!...")
