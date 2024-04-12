from django.contrib import admin

from .models import Activity, Company, JobPosting, Application, Interview, Offer

admin.site.register(Activity)
admin.site.register(Company)
admin.site.register(JobPosting)
admin.site.register(Application)
admin.site.register(Interview)
admin.site.register(Offer)
