from django.db import models
from django.utils import timezone


class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    task_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    celery_task_id = models.CharField(max_length=50, blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} ({self.status})"
        
    def mark_as_started(self):
        self.status = 'in_progress'
        self.started_at = timezone.now()
        self.save()
    
    def mark_as_completed(self, result=None):
        self.status = 'completed'
        self.completed_at = timezone.now()
        if result:
            self.result = str(result)
        self.save()
    
    def mark_as_failed(self, error=None):
        self.status = 'failed'
        self.completed_at = timezone.now()
        if error:
            self.result = str(error)
        self.save()