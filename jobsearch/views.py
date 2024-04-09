from django.shortcuts import render
from django.views.generic import ListView

from .models import Activity

class HomePageView(ListView):
    model = Activity
    template_name = 'jobsearch/home.html'
    context_object_name = 'activities'
