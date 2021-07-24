from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from dashboard.views import students, evaluations
from login.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('students/', students),
    path('evaluations', evaluations),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
