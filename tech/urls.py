from django.urls import path
from . import views




urlpatterns = [
    path('blogs-list',views.BlogListView, name='blog-list-view'),
    path('<int:id>',views.BlogDetail, name='blog-detail'),
    path('home',views.home, name='home-page'),
    path('post/<int:id>', views.PostDetailView, name='post-detail-view'),
    path('user-profile/<str:username>', views.UserProfile, name='user-profile'),
]















