from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'task_type', 'status', 'created_at', 'started_at', 'completed_at')
    list_filter = ('status', 'task_type')
    search_fields = ('name', 'description')
    readonly_fields = ('celery_task_id', 'created_at', 'updated_at', 'started_at', 'completed_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'task_type')
        }),
        ('Status Information', {
            'fields': ('status', 'result')
        }),
        ('Task Details', {
            'fields': ('celery_task_id', 'created_at', 'updated_at', 'started_at', 'completed_at')
        }),
    )