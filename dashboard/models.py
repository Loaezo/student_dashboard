from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class StudentDetails(models.Model):
    class Meta:
        verbose_name = 'detail'
        verbose_name_plural = 'Student details'
    FIRST_YEAR = '1'
    SECOND_YEAR = '2'
    THIRD_YEAR = '3'
    YEAR_IN_SCHOOL_CHOICES = [
        (FIRST_YEAR, 'First year'),
        (SECOND_YEAR, 'Second year'),
        (THIRD_YEAR, 'Third year'),
    ]
    year = models.CharField(
        max_length=1,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default='1'
    )
    GROUP_A = 'A'
    GROUP_B = 'B'
    GROUP_C = 'C'
    SCHOOL_GROUP_CHOICES = [
        (GROUP_A, 'Group A'),
        (GROUP_B, 'Group B'),
        (GROUP_C, 'Group C'),
    ]
    group = models.CharField(
        max_length=1,
        choices=SCHOOL_GROUP_CHOICES,
        default=GROUP_A
    )
    subject = models.CharField(max_length=64, null=True)
    grade = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=1)
    student = models.ForeignKey(User, on_delete=models.CASCADE)