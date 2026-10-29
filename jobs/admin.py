from django.contrib import admin
from .models import Company, JobListing, Application

admin.site.register(Company)
admin.site.register(JobListing)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job', 'email', 'phone', 'created_at')
    search_fields = ('full_name', 'email', 'job__title')