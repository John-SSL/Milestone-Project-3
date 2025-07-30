from django.shortcuts import render

# Create your views here.

def job_tracker(request):
    return render(request, "job_tracker/job-tracker.html")