from django import forms
from .models import CompletedJob

class CompletedJobForm(forms.ModelForm):
    class Meta:
        model = CompletedJob
        fields = ('job_type', 'completed_on')
        widgets = {'completed_on': forms.DateInput(attrs={'type': 'date'}),}