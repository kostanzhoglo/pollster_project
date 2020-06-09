from django.urls import path

from . import views

app_name = 'polls'

url_patterns = [
    # the '' on the next line actually means 'polls/'.
    # if instead we put, 'result' it would be 'polls/result'
    path('', views.index, name='index')
]
