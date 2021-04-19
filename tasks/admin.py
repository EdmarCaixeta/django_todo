from django.contrib import admin
from .models import *

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "complete", "created", "updated"]

admin.site.register(Task, TaskAdmin)