from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from .tasks import process_task

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']
    paginate_by = 10

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task-list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Get the saved object
        task = self.object
        
        # Submit task to Celery
        process_task.delay(task.id)
        
        messages.success(self.request, f'Task "{task.name}" created and queued for processing!')
        return response