from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from dashboard.models import StudentDetails
from dashboard.forms import RegisterForm


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'dashboard/signup.html', {'form': form})


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