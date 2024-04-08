from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .models import Booking
from . import utils

class HomePageView(TemplateView):
    template_name = 'timetracking/home.html'
    
    
class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = ['date', 'start_time', 'end_time', 'category', 'comment']
    template_name = 'timetracking/booking_new.html'
    success_url = '/timetracking/home'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse("booking_list")
      
class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'timetracking/booking_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        
        context["booking_list"] = Booking.objects.filter(user=self.request.user)
        
        date_ranges = utils.get_date_ranges_of_last_n_days(3)
        daily_overview = {}
        for date_range in date_ranges:
            start_date, end_date = date_range
            bookings = utils.get_bookings_in_date_range(start_date, end_date, self.request.user)
            daily_overview[start_date.strftime("%d.%m.%y")] = utils.get_duration_per_category(bookings)
        context["daily_overview"] = daily_overview
        context["user"] = self.request.user
    
        date_ranges = utils.get_date_ranges_of_last_n_weeks(3)
        weekly_overview = {}
        for date_range in date_ranges:
            start_date, end_date = date_range
            bookings = utils.get_bookings_in_date_range(start_date, end_date, self.request.user)
            weekly_overview[start_date.strftime("%d.%m.%y")] = utils.get_duration_per_category(bookings)
        context["weekly_overview"] = weekly_overview
        context["user"] = self.request.user
    
        date_ranges = utils.get_date_ranges_of_last_n_months(3)
        monthly_overview = {}
        for date_range in date_ranges:
            start_date, end_date = date_range
            bookings = utils.get_bookings_in_date_range(start_date, end_date, self.request.user)
            monthly_overview[start_date.strftime("%b %Y")] = utils.get_duration_per_category(bookings)
        context["monthly_overview"] = monthly_overview
        return context
        
        

        
class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    fields = ['date', 'start_time', 'end_time', 'category', 'comment']
    template_name = 'timetracking/booking_edit.html'
    success_url = '/timetracking/booking/list'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'timetracking/booking_delete.html'
    success_url = '/timetracking/booking/list'
    
    def get_success_url(self) -> str:
        return reverse('booking_list')