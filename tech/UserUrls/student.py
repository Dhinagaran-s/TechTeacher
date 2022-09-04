from django.contrib import admin
from django.urls import path, include

from tech.UserPermission import student as views



urlpatterns = [


    path('profile/<str:username>', views.StudentPublicProfile, name='student-public-profile'),
    path('<str:username>/account', views.StudentPersonalProfile, name='student-personal-profile'),
    path('<str:username>/account/profile-update', views.StudentProfileUpdate, name='student-profile-update'),
    path('student-list', views.StudentStudentList, name='student-student-list'),
    path('staff-list', views.StudentStaffList, name="student-staff-list"),
    path('my-posts', views.StudentSelfPosts, name='student-self-post-list'),






]


