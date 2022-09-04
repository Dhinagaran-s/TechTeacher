from django.urls import path, include
from . import views




urlpatterns = [

    ### BASIC

    
    ### BLOG
    path('blogs-list',views.PostListView, name='post-list-view'),
    path('<int:id>',views.PostDetail, name='post-detail'),
    path('home',views.home, name='home-page'),
    path('post/<int:id>', views.PostDetailView, name='post-detail-view'),
    path('post/create', views.PostCreateView, name='post-create-view'),
    path('post/create-save', views.PostCreateSave, name='post-create-save'),
    path('post/update/<int:id>', views.PostUpdateView, name='post-update-view'),
    path('post/update-save/<int:id>',views.PostUpdateSave, name='post-update-save' ),
    path('self-post/',views.SelfPost, name='self-post'),
    path('staff-list',views.StaffList, name='staff-list'),
    path('student-list',views.StudentList, name='student-list'),






]















