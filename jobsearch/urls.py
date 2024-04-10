from django.urls import path
from .views import HomePageView, ActivityDetailView


urlpatterns = [
    path('', HomePageView.as_view(), name='jobsearch_home'),
    path('activity/<uuid:pk>', ActivityDetailView.as_view(), name='activity_detail'),
]