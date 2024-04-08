from datetime import datetime
from dateutil.relativedelta import relativedelta

import calendar

from .models import Booking

def get_bookings_in_date_range(start_date, end_date, user):
    """
    Get all bookings of a user in a date range.
    """
    return Booking.objects.filter(date__gte=start_date, date__lte=end_date, user=user)

def get_duration_per_category(bookings) -> dict:
    """
    Calculate the total duration per category for a list of bookings.
    
    return: A dictionary with the category as key and the total duration as value.
    """
    categories = {}
    for booking in bookings:
        if booking.category in categories.keys():
            categories[booking.category] += booking.duration
        else:
            categories[booking.category] = booking.duration
    
    categories = dict(sorted(categories.items(), key=lambda item: item[1], reverse=True))

    return categories

def get_month_date_range(date):
    """
    Get the date range of a month.
    """
    _, last_day = calendar.monthrange(date.year, date.month)
    start_date = date.replace(day=1)
    end_date = date.replace(day=last_day)
    return start_date, end_date

def get_date_ranges_of_last_n_months(n):
    """
    Get the date ranges of the last n months.
    """
    date_ranges = []
    for i in range(n):
        date = datetime.now().date().replace(day=1)
        date = date - relativedelta(months=i)
        date_ranges.append(get_month_date_range(date))
    return date_ranges

def get_date_ranges_of_last_n_weeks(n) -> list:
    """
    Get the date ranges of the last n weeks.
    
    return: A list of tuples with the start and end date of a week.
    """
    date_ranges = []
    for i in range(n):
        date = datetime.now().date()
        start_date = date - relativedelta(weeks=i, weekday=0)
        end_date = date - relativedelta(weeks=i, weekday=6)
        date_ranges.append((start_date, end_date))
    return date_ranges

def get_date_ranges_of_last_n_days(n) -> list:
    """
    Get the date ranges of the last n days.
    
    return: A list of tuples with the start and end date of a day.
    """
    date_ranges = []
    for i in range(n):
        date = datetime.now().date()
        start_date = date - relativedelta(days=i)
        end_date = date - relativedelta(days=i)
        date_ranges.append((start_date, end_date))
    return date_ranges
