from django.contrib import admin

# Register your models here.
from tracker.models import Task, Status, Type


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'status', 'date_created', 'date_updated']


admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Task, TaskAdmin)

