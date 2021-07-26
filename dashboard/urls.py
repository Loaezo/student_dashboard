from django.urls import path

from dashboard import views


urlpatterns = [
    path('students/', views.students, name='students'),
    path('evaluations/', views.evaluations, name='evaluations'),
]