from django.urls import path
from . import views



urlpatterns = [
    path('post/<int:id>', views.PostsDetailViewAPI, name='post-detail-api'),
    path('posts/', views.SearchPostsListAPIView.as_view(), name='search-posts'),
    path('author/<int:id>', views.AuthorDetails, name='author-details'),
]



















































