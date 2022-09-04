from django.contrib import admin
from django.urls import path, include

from tech.UserPermission import staff as views




urlpatterns = [

    path('profile/<str:username>', views.StaffPublicProfile, name='staff-public-profile'),
    path('<str:username>/account', views.StaffPersonalProfile, name='staff-personal-profile'),
    path('<str:username>/account/profile-update', views.StaffProfileUpdate, name='staff-profile-update'),
    path('student-list', views.StaffStudentList, name='staff-student-list'),
    path('staff-list', views.StaffStaffList, name="staff-staff-list"),
    path('my-posts', views.StaffSelfPosts, name='staff-self-post-list'),


]

