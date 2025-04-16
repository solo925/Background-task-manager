from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'task_type']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['task_type'].widget = forms.Select(choices=(
            ('data_processing', 'Data Processing'),
            ('email_campaign', 'Email Campaign'),
            ('report_generation', 'Report Generation'),
            ('other', 'Other'),
        ))