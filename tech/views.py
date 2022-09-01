from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.models import AbstractUser
from django.contrib import messages
from tech.EmailBackEnd import EmailBackEnd

from .models import CustomUser, Posts


# Create your views here.




def PostListView(request):
    blog_list = Posts.objects.all()
    return HttpResponse(blog_list)



def PostDetail(request, id):
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

def PostCreateView(request):
    return render(request, 'blog/blog_create.html')



def PostCreateSave(request):
    if request.method != 'POST':
        return HttpResponse('You are not allowed to do this')

    title = request.POST.get('title')
    sub_title = request.POST.get('sub-title')
    content = request.POST.get('content')

    user = CustomUser.objects.get(id=request.user.id)

    post_obj = Posts(title=title, sub_title=sub_title, body=content, created_by=user)
    post_obj.save()

    return HttpResponseRedirect(reverse('post-detail-view', kwargs={'id':post_obj.id} ))



def LoginPage(request):
    return render(request, 'basic/login.html')

def IllegalAccess(reqeust):
    return HttpResponse('You are not allowed to do this')


def LoginUser(request):
    if request.method != 'POST':
        IllegalAccess(request)
    user = EmailBackEnd.authenticate(request, email=request.POST.get('email'), password=request.POST.get('password'))

    if user != None:
        login(request, user)
        return HttpResponseRedirect(reverse('home-page'))
    messages.error(request, 'Please check login credintials !')
    return redirect('login-page')


def LogoutUser(request):
    if request.method != 'GET':
        IllegalAccess(request)
    logout(request)
    messages.success(request, 'Logged Out !')
    return redirect('login-page')


def RegisterPage(request):
    return render(request, 'basic/register.html')


def RegisterStudentUser(request):
    if request.method != 'POST':
        IllegalAccess(request)
    first_name = request.POST.get('first-name')
    last_name = request.POST.get('last-name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    username = email.split('@')[0]

    
    if password2 != password:
        messages.error(request, "Password didn't match")
        return redirect('register-page')
    
    if email != None and last_name != None and first_name != None:
        UserModel = get_user_model()
        try:
            UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=3)
            user.studentuser.college = 'University College of Engineering Kanchipuram'
            user.save()
            messages.success(request, 'Registered User')
            return redirect('login-page')
    messages.error(request, "User already exists")    
    return redirect('register-page')








def terms_and_conditions(request):
    return render(request, 'basic/terms-and-conditions.html')



def UserPublicProfile(request,username):
    user = CustomUser.objects.get(username=username)
    return render(request, 'basic/public-profile.html',{'data':user})











