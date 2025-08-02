from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class JobType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    credits = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.credits} credits)"


class CompletedJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    completed_on = models.DateField()


class Absence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.user} absent for {self.duration} hours on {self.date}"


class ProfileTarget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    daily_target = models.DecimalField(max_digits=3, decimal_places=2, default=4.25)

    def __str__(self):
        return f"Engineer:{self.user}, Target:{self.daily_target}"