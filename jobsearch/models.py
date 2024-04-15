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
      

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    headhunter = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Companies'
        
    def __str__(self):
        return self.name
      
class JobPosting(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
    CHOICES = (
        ('On-site', 'On-site'),
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
    )
    type = models.CharField(max_length=20, choices=CHOICES, default='On-site')
    location = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['company', 'title']
        verbose_name_plural = 'Job Postings'
        
    def __str__(self):
        return self.title
      
class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    date = models.DateField()
    CHOICES = (
        ('Applied', 'Applied'),
        ('Rejected', 'Rejected'),
        ('No response', 'No response'),
        ('Interviewing', 'Interviewing'),
        ('Offered', 'Offered'),
        ('Offer accepted', 'Offer accepted'),
        ('Offer rejected', 'Offer rejected'),
    )
    status = models.CharField(max_length=20, choices=CHOICES, default='Applied')
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Applications'
        
    def __str__(self):
        return f'Application for {self.job_posting} on {self.date.strftime("%d %b %Y")} - status: {self.status}'
      
class Interview(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    CHOICES = (
        ('Virtual', 'Virtual'),
        ('In person', 'In person'),
    )
    type = models.CharField(max_length=20, choices=CHOICES, default='Virtual')
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-time']
        verbose_name_plural = 'Interviews'
        
    def __str__(self):
        return f'Inteview on {self.date.strftime("%d %b %Y")}'
      
class Offer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    date = models.DateField()
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True, null=True)
    CHOICES = (
        ('Response pending', 'Response pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )
    status = models.CharField(max_length=20, choices=CHOICES, default='Response pending')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Offers'
        
    def __str__(self):
        return f'Offer as {self.position} received on {self.date.strftime("%d %b %Y")} - status: {self.status}'