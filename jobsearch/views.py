from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView


from .models import Activity

class HomePageView(ListView):
    model = Activity
    template_name = 'jobsearch/home.html'
    context_object_name = 'activities'

class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'jobsearch/activity_detail.html'
    context_object_name = 'activity'
    
class ActivityUpdateView(UpdateView):
    model = Activity
    fields = ['headline', 'date', 'description', 'next_steps', 'reminder_date']
    template_name = 'jobsearch/activity_update.html'
    
    def get_success_url(self) -> str:
        return reverse("activity_detail", kwargs={"pk": self.object.pk})