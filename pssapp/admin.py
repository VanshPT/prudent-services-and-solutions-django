from django.contrib import admin
from .models import Contacts,JobEntry,JobDetail,JobApplications
# Register your models here.
admin.site.register(Contacts)
admin.site.register(JobEntry)
admin.site.register(JobDetail)
admin.site.register(JobApplications)