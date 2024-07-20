from django.contrib import admin

from jobs.models import Jobs, Application, Company

# Register your models here.
admin.site.register(Jobs)
admin.site.register(Company)
admin.site.register(Application)