from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from dashboard.models import StudentDetails


@login_required
def students(request):
    return render(request, 'dashboard/dashboard.html',
                  {'StudentDetails': StudentDetails.objects.all()})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('students')
        else:
            return render(request, 'dashboard/home.html', {'error': 'Invalid user and/or password'})
    return render(request, 'dashboard/home.html',
                  {'StudentDetails': StudentDetails.objects.all()})


@login_required
def evaluations(request):
    return render(request, 'dashboard/evaluations.html',
                  {'StudentDetails': StudentDetails.objects.all()})
