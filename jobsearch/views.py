from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView


from .models import Activity

class HomePageView(ListView):
    model = Activity
    template_name = 'jobsearch/home.html'
    context_object_name = 'activities'

class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'jobsearch/activity_detail.html'
    context_object_name = 'activity'
    
