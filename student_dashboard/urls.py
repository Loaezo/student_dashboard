from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dashboard.views import login_view, logout_view, signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', include('dashboard.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
