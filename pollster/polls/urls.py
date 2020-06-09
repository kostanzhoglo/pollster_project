from django.urls import path

from . import views

app_name = 'polls'

url_patterns = [
    path('', views.index, name='index')
]
