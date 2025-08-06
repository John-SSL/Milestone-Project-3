from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from django.views import generic
from datetime import date, timedelta
from .forms import CompletedJobForm
from .models import CompletedJob, Absence

# Create your views here.

def job_tracker(request):
    user = request.user
    today = date.today()
    start_of_week = today - timedelta(days= today.weekday())
    end_of_week = start_of_week + timedelta(days=4)

    jobs = CompletedJob.objects.filter(user = user, completed_on__range=
    (start_of_week, end_of_week)).values('completed_on').annotate(total_credits=Sum('job_type__credits'))
    
    # Creates dict with the completed jobs of the current week {date:credits}
    credits_by_day = {start_of_week + timedelta(days=i): 0 for i in range(7)}
    for entry in jobs:
        credits_by_day[entry['completed_on']] = float(entry["total_credits"])
    
    # Gets user's absences for current week and creates dict with the day and duration
    absences = Absence.objects.filter(user = user, date__range=(start_of_week, end_of_week))
    absences_by_day = {a.date: float(a.duration) for a in absences}
    
    # Calculates target and creates dict with day and the target
    daily_target = float(user.profiletarget.daily_target)
    adjusted_targets = {}
    shift_hours = 8
    for i in range(5):
        current_day = start_of_week + timedelta(days=i)
        absence = absences_by_day.get(current_day, 0)
        adjusted = round(((shift_hours - absence) * daily_target) / shift_hours, 2)
        adjusted_targets[current_day] = adjusted
    
    # Store all of the combined metrics for the week
    weekly_data = []
    for i in range(5):
        current_day = start_of_week + timedelta(days=i)
        weekly_data.append({
            "date": current_day,
            "target": adjusted_targets[current_day],
            "credits": credits_by_day[current_day]
        })
    
    # Create a form for submitting completed jobs
    if request.method == "POST":
        job_form = CompletedJobForm(request.POST)
        if job_form.is_valid():
            form = job_form.save(commit=False)
            form.user = user
            form.save()
            messages.add_message(request, messages.SUCCESS, 'New job submitted')
            return redirect('tracker')

    job_form = CompletedJobForm()
    return render(
        request,
        "job_tracker/job-tracker.html",
        {"weekly_data": weekly_data,
         "job_form": job_form,
         })


class CompletedJobList(generic.ListView):
    model = CompletedJob
    template_name = "job_tracker/job-history.html"
    paginate_by = 7
    def get_queryset(self):
        return CompletedJob.objects.filter(user = self.request.user)