from django.db import models
import uuid

class Activity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    headline = models.CharField(max_length=50)
    description = models.TextField()
    next_steps = models.TextField(blank=True, null=True)
    reminder_date = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Activities'
        
    def __str__(self):
        return self.headline
      
