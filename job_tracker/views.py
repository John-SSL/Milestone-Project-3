from django.shortcuts import render,get_object_or_404
from django.db.models import Sum
from datetime import date, timedelta
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
    
    return render(
        request,
        "job_tracker/job-tracker.html",
        {"weekly_data": weekly_data,
         })

    
    # jobs = get_object_or_404(queryset, pk = 2 )
    # user = request.user
    # today = date.today()
    # start_of_week = today - timedelta(days=today.weekday())
    # end_of_week = start_of_week + timedelta(days=6)
    # queryset = CompletedJob.objects.filter(user = user, completed_on__range = (start_of_week, end_of_week))
    # print(f"Printing completed jobs:{queryset}")