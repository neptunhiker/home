from django.views.generic import TemplateView, CreateView
from .models import Booking

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class ReportsView(TemplateView):
    template_name = 'reports.html'
    
class BookingCreateView(CreateView):
    model = Booking
    fields = ['date', 'start_time', 'end_time', 'category', 'comment']
    template_name = 'booking_new.html'
    success_url = '/timetracking/home'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)