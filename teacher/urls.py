"""teacher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from teacher import settings
from tech import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('ckeditor/',include('ckeditor_uploader.urls')),

    path('blog/',include('tech.urls')),
    path('api/', include('tech.api.urls')),
    path('administration/',include('tech.UserUrls.admin')),
    path('staff/',include('tech.UserUrls.staff')),
    path('student/',include('tech.UserUrls.student')),

    path('login', views.LoginPage, name='login-page'),
    path('login-user', views.LoginUser, name='login-user'),
    path('logout-user',views.LogoutUser, name='logout-user'),

    path('staff/register',views.StaffRegisterPage, name='register-staff-page'),
    path('staff/register/save', views.StaffRegister, name='register-staff-user'),

    path('student/register',views.StudentRegisterPage, name='register-student-page'),
    path('student/register/save', views.StudentRegister, name='register-student-user'),    
        
    path('report',views.ReportPage, name='report-page'),
    path('report-save',views.ReportSave, name='report-save'),


    path('<str:username>/account/change-password',views.UserPasswordChange, name='user-change-password'),
    path('user/<str:username>/dashboard',views.UserTypeRedirect, name='user-dashboard'),

    path('terms-and-conditions', views.terms_and_conditions, name='terms-and-conditions'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
