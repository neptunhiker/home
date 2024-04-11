from django.urls import path
from .views import HomePageView, ActivityDetailView, ActivityUpdateView, ActivityCreateView


urlpatterns = [
    path('', HomePageView.as_view(), name='jobsearch_home'),
    path('activity/<uuid:pk>', ActivityDetailView.as_view(), name='activity_detail'),
    path('activity/edit/<uuid:pk>', ActivityUpdateView.as_view(), name='activity_edit'),
    path('activity/new', ActivityCreateView.as_view(), name='activity_new'),
]