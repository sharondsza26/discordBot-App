from django.contrib import admin
from django.urls import path
from .quiz.views import RandomQuestion

urlpatterns = [
    path('admin/', admin.site.urls),
    # pointing bot to the system
    # when it connects to api/random, bot will point to views.py
    path('api/random/', RandomQuestion.as_view(), name='random'),
]
