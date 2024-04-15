from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from .models import Activity, Company, JobPosting, Application, Interview, Offer
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin, ListView):
  model = Activity
  template_name = 'jobsearch/home.html'
  context_object_name = 'activities'

class ActivityDetailView(LoginRequiredMixin, DetailView):
  model = Activity
  template_name = 'jobsearch/activity_detail.html'
  context_object_name = 'activity'
  
class ActivityUpdateView(LoginRequiredMixin, UpdateView):
  model = Activity
  fields = ['headline', 'date', 'description', 'next_steps', 'reminder_date', 'reminder_completed']
  template_name = 'jobsearch/activity_update.html'
  
  def get_success_url(self) -> str:
    return reverse("activity_detail", kwargs={"pk": self.object.pk})
      
class ActivityCreateView(LoginRequiredMixin, CreateView):
    model = Activity
    fields = ['headline', 'date', 'description', 'next_steps', 'reminder_date']
    template_name = 'jobsearch/activity_new.html'
    
    def get_success_url(self) -> str:
        return reverse("jobsearch_home")
      
class ActivityDeleteView(LoginRequiredMixin, DeleteView):
    model = Activity
    template_name = 'jobsearch/activity_delete.html'
    
    def get_success_url(self) -> str:
        return reverse("jobsearch_home")
      
class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'jobsearch/company_list.html'
    context_object_name = 'companies'
    
