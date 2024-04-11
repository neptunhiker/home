from django.db import models
import uuid

from django.urls import reverse

class Activity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    headline = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField()
    next_steps = models.TextField(blank=True, null=True)
    reminder_date = models.DateField(blank=True, null=True)
    reminder_completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('activity_detail', args=[str(self.id)])
      
    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Activities'
        
    def __str__(self):
        return self.headline
      
