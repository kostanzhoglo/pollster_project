from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

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

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

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
    return render(request, 'polls/detail.html', { 'question': question })

# Get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', { 'question': question })

# Vote for a question choice
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))