from django.shortcuts import render
from django.http.response import HttpResponse

from .models import CustomUser, Posts


# Create your views here.




def BlogListView(request):
    blog_list = Posts.objects.all()
    return HttpResponse(blog_list)



def BlogDetail(request, id):
    blog = Posts.objects.get(id=id)
    return HttpResponse(blog.body)

def home(request):
    posts = Posts.objects.all()
    return render(request,'blog/home.html',{'post':posts})


def PostDetailView(request,id):
    post = Posts.objects.get(id=id)
    return render(request, 'blog/blog_detail.html',{'post':post})


def UserProfile(request, username):
    user = CustomUser.objects.get(username=username)
    return render(request, 'portfolio/student/PersonalProfile.html')



























