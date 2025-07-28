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