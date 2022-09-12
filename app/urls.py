
from django.urls import path

from app.views import index, search_word

urlpatterns = [
    path('', index),
    path('search_word/', search_word)
]