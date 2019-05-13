from django.contrib import admin
from . import models

admin.site.site_header = 'Laboratory app admin'

# Register your models here.
admin.site.register(models.SampleType)
admin.site.register(models.Sample)
