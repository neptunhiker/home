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
        verbose_name="Nutzer"
    )
    date = models.DateField(verbose_name="Datum")
    start_time = models.DateTimeField(verbose_name="Startzeit")
    end_time = models.DateTimeField(verbose_name="Endzeit")
    CATEGORIES = (
        ('Arbeit', 'Arbeit'),
        ('Pause', 'Pause'),
        ('Jobsuche', 'Jobsuche')
        ('Freizeit', 'Freizeit'),
        ('Urlaub', 'Urlaub'),
        ('Krankheit', 'Krankheit'),
        ('Sonstiges', 'Sonstiges'),
    )
    category = models.CharField(max_length=20, choices=CATEGORIES, default='Arbeit')
    comment = models.TextField()
    
    def __str__(self):
        return f'{self.user} - {self.start_time} bis {self.end_time} am {self.date}'