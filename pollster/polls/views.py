from django.shortcuts import render

# Create your views here.

# import your models, otherwise you'll never know what to render in the 1st place
from .models import Question, Choice

# Get Questions and display them
def index(request):
    # This will pass in our Questions list to the index.html page, so that info will be displayed
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    # this will return a basic template.
    # 1st param == Passing in the request object, 
    # 2nd param == location of the template. 
    # This does NOT create the template itself OR the URL needed. More work to do!
        # Inside polls folder, create a urls.py to make the URL.
    return render(request, 'polls/index.html', context)

# Show specific question and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/results.html', { 'question': question })