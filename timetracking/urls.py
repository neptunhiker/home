from django.urls import path
from .views import HomePageView, ReportsView, BookingCreateView

urlpatterns = [
    path('home', HomePageView.as_view(), name='home'),
    path('reports', ReportsView.as_view(), name='reports'),
    path('booking/new', BookingCreateView.as_view(), name='booking_new'),
]