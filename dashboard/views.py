from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from dashboard.models import StudentDetails
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


@login_required
def students(request):
    return render(request, 'dashboard/dashboard.html',
                  {'StudentDetails': StudentDetails.objects.all()})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('students')
    else:
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


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request, 'dashboard/signup.html', {'error': 'The passwords entered do not match'})

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'dashboard/signup.html', {'error': 'The username is already taken'})
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        return redirect('login')
    return render(request, 'dashboard/signup.html')