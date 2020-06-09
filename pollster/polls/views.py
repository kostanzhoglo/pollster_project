from django.shortcuts import render

# Create your views here.

# import your models, otherwise you'll never know what to render in the 1st place
from .models import Question, Choice