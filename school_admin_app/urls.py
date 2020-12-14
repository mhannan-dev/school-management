"""project_src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import hodViews
from . import staffViews
from . import studentViews



urlpatterns = [
    path('login_page_show', views.login_page_show, name='login_page_show'),
    path('login', views.user_login, name = 'user_login'),
    path('get_user_details', views.get_user_details, name='get_user_details'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('admin_dashboard', hodViews.admin_dashboard, name='admin_dashboard'),
    path('staff_dashboard', staffViews.staff_dashboard, name='staff_dashboard'),
    path('student_dashboard', studentViews.student_home, name='student_home'),





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

