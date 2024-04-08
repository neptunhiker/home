from .models import Booking

def get_bookings_in_time_range(start_date, end_date, user):
    """
    Get all bookings of a user in a time range.
    """
    return Booking.objects.filter(date__gte=start_date, date__lte=end_date, user=user)

def get_duration_per_category(bookings):
    """
    Calculate the total duration per category for a list of bookings.
    """
    categories = {}
    for booking in bookings:
        if booking.category in categories:
            categories[booking.category] += booking.duration
        else:
            categories[booking.category] = booking.duration
    return categories