from django.db import models
from django.contrib.auth.models import User


class Dashboard(models.Model):
    subject = models.CharField(max_length=64, null=True)
    grade = models.FloatField(null=False, default=1)
    year = models.IntegerField(null=False, default=1)
    group = models.CharField(max_length=1, null=False, default='A')
    student = models.ForeignKey(User, on_delete=models.CASCADE)