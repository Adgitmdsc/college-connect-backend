from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.College)
admin.site.register(models.Society)
admin.site.register(models.Faculty)
admin.site.register(models.Student)