from django.urls import path
from .views import HomePageView, ReportsView

urlpatterns = [
    path('home', HomePageView.as_view(), name='home'),
    path('reports', ReportsView.as_view(), name='reports'),
]