from django import forms
from .models import CompletedJob, Absence

class CompletedJobForm(forms.ModelForm):
    class Meta:
        model = CompletedJob
        fields = ('job_type', 'completed_on')
        widgets = {'completed_on': forms.DateInput(attrs={'type': 'date'}),}


class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ('duration', 'date')
        widgets = {'date': forms.DateInput(attrs={'type': 'date'}),}