from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
import uuid 

class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="User"
    )
    date = models.DateField(verbose_name="Date")
    start_time = models.TimeField(verbose_name="Starting time")
    end_time = models.TimeField(verbose_name="Ending time")
    CATEGORIES = (
        ('Work', 'Work'),
        ('Break', 'Break'),
        ('Job search', 'Job search'),
        ('Leisure', 'Leisure'),
        ('Vacation', 'Vacation'),
        ('Illness', 'Illness'),
        ('Other', 'Other'),
    )
    category = models.CharField(max_length=20, choices=CATEGORIES, default='Work')
    comment = models.TextField()
    
    def __str__(self):
        return f'{self.user} - {self.start_time} until {self.end_time} on {self.date}'