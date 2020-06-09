from django.shortcuts import render

# Create your views here.

# import your models, otherwise you'll never know what to render in the 1st place
from .models import Question, Choice

# Get Questions and display them
def index(request):
    # this will return a basic template.
    # 1st param == Passing in the request object, 
    # 2nd param == location of the template. 
    # This does NOT create the template itself OR the URL needed. More work to do!
        # Inside polls folder, create a urls.py to make the URL.
    return render(request, 'polls/index.html')