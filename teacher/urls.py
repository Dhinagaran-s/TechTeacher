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

from tech import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('blog/',include('tech.urls')),

    path('login', views.LoginPage, name='login-page'),
    path('login-user', views.LoginUser, name='login-user'),
    path('logout-user',views.LogoutUser, name='logout-user'),

    path('register',views.RegisterPage, name='register-page'),
    path('register-user',views.RegisterStudentUser, name='register-user-student'),


    path('user-profile/<str:username>', views.UserProfile, name='user-profile'),
    path('user/<str:username>', views.UserPublicProfile, name='user-public-profile'),


    path('terms-and-conditions', views.terms_and_conditions, name='terms-and-conditions'),
]
