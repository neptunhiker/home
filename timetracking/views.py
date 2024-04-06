from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .models import Booking

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class ReportsView(TemplateView):
    template_name = 'reports.html'
    
class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = ['date', 'start_time', 'end_time', 'category', 'comment']
    template_name = 'booking_new.html'
    success_url = '/timetracking/home'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
      
class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["booking_list"] = Booking.objects.filter(user=self.request.user)
        context["user"] = self.request.user
        return context
        
class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    fields = ['date', 'start_time', 'end_time', 'category', 'comment']
    template_name = 'booking_edit.html'
    success_url = '/timetracking/booking/list'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'booking_delete.html'
    success_url = '/timetracking/booking/list'
    
    def get_success_url(self) -> str:
        return reverse('booking_list')