from django.shortcuts import render
from django.http import HttpResponse


def students(request):
    return render(request, 'dashboard/dashboard.html')


def evaluations(request):
    return render(request, 'dashboard/evaluations.html')