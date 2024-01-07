from django.urls import path

from .views import quiz

urlpatterns = [
    path('', quiz, name='quiz'),
]