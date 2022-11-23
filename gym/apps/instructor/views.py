from django.shortcuts import render
from django.http import HttpResponse

from .models import Instructor


def index(request):
    return HttpResponse("Instructor's urls works!...")
