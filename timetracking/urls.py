from django.urls import path
from .views import HomePageView, BookingCreateView, BookingListView, BookingUpdateView, BookingDeleteView


urlpatterns = [
    path('', HomePageView.as_view(), name='timetracking_home'),
    path('booking/new', BookingCreateView.as_view(), name='booking_new'),
    path('booking/list', BookingListView.as_view(), name='booking_list'),
    path('booking/edit/<uuid:pk>', BookingUpdateView.as_view(), name='booking_edit'),
    path('booking/delete/<uuid:pk>', BookingDeleteView.as_view(), name='booking_delete'),
]