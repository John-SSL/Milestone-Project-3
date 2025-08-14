from django.urls import path
from . import views 

urlpatterns = [
    path('', views.job_tracker, name='tracker'),
    path('absences', views.AbsencesList.as_view(), name='absences'),
    path('history', views.CompletedJobList.as_view(), name='job-history'),
    path('history/update/<int:pk>', views.job_edit, name='update-completed-job'),
    path('history/delete/<int:pk>', views.job_delete, name='delete-completed-job'),
]