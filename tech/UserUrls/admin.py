from django.contrib import admin
from django.urls import path, include

from tech.UserPermission import admin as views





urlpatterns = [

    path('profile/<str:username>', views.AdminPublicProfile, name='admin-public-profile'),
    path('<str:username>/account', views.AdminPersonalProfile, name='admin-personal-profile'),
    path('<str:username>/account/profile-update', views.AdminProfileUpdate, name='admin-profile-update'),
    path('student-list', views.AdminStudentList, name='admin-student-list'),
    path('staff-list', views.AdminStaffList, name="admin-staff-list"),
    path('my-posts', views.AdminSelfPosts, name='admin-self-post-list'),
    path('report-list', views.ReportListView, name='report-list'),
    path('report-detail-view/<int:id>', views.ReportDetailView, name='report-detail-view'),

]











