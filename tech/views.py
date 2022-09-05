from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, get_user_model
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

from tech.EmailBackEnd import EmailBackEnd
from .models import CustomUser, Posts, Reports


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




def AdminPersonalProfile(request, username):
    UserChecking(request, username)
    return render(request, 'portfolio/admin/personal-profile.html')




def PostCreateView(request):
    return render(request, 'blog/blog_create.html')

def PostUpdateView(request, id):
    post = Posts.objects.get(id=id)
    return render(request, 'blog/blog_update.html', {'post':post})

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


def PostUpdateSave(request, id):
    if request.method != 'POST':
        return HttpResponse('You are not allowed to do this')

    title = request.POST.get('title')
    sub_title = request.POST.get('sub-title')
    content = request.POST.get('content')

    post = Posts.objects.get(id=id)

    post.title = title
    post.sub_title = sub_title
    post.body = content
    post.save()

    return HttpResponseRedirect(reverse('post-detail-view', kwargs={'id':post.id} ))

    


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


def UserTypeRedirect(request, username):
    if request.method != 'GET':
        IllegalAccess(request)
    if request.user.user_type == '1':
        return HttpResponseRedirect(reverse('admin-personal-profile', kwargs={'username':username}))
    if request.user.user_type == '2':
        return HttpResponseRedirect(reverse('staff-personal-profile', kwargs={'username':username}))
    if request.user.user_type == '3':
        return HttpResponseRedirect(reverse('student-personal-profile', kwargs={'username':username}))
    return redirect('login-page')



def LogoutUser(request):
    if request.method != 'GET':
        IllegalAccess(request)
    logout(request)
    messages.success(request, 'Logged Out !')
    return redirect('login-page')




def terms_and_conditions(request):
    return render(request, 'basic/terms-and-conditions.html')


def AdminPublicProfile(request, username):
    user = CustomUser.objects.get(username=username)
    if user.user_type != '1':
        IllegalAccess(request)
    return render(request, 'portfolio/admin/public-profile.html',{'data':user})





def UserChecking(request, username):
    if request.user.username != username:
        IllegalAccess(request)
    





def AdminProfileUpdate(request, username):
    if request.method != 'POST':
        IllegalAccess(request)
    UserChecking(request, username)

    user = CustomUser.objects.get(id=request.user.id)
    user.first_name = request.POST.get('firstname')
    user.last_name = request.POST.get('lastname')
    user.save()

    messages.success(request, 'Profile Updated !')
    return HttpResponseRedirect(reverse('user-profile',kwargs={'username':username}))





def UserPasswordChange(request, username):
    if request.method != 'POST':
        IllegalAccess(request)
    UserChecking(request, username)
    print('user checking completed')

    current_password = request.POST.get('password')
    new_password = request.POST.get('newpassword')
    re_new_password = request.POST.get('renewpassword')

    if current_password != '' and new_password != '' and re_new_password != '' :

        if new_password != re_new_password:
            messages.error(request, "Passwords didn't match ")
            return HttpResponseRedirect(reverse('user-profile',kwargs={'username':username}))
        
        UserModel = get_user_model()
        user=UserModel.objects.get(email=request.user.email)
        if user.check_password(current_password):
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password changed !')
            # return HttpResponseRedirect(reverse('user-profile',kwargs={'username':username}))
            return redirect('login-page')
        messages.error(request, 'Incorrect passowrd')
        return HttpResponseRedirect(reverse('user-profile',kwargs={'username':username}))
    messages.error(request, 'Please fill all fields inorder to change password')
    return HttpResponseRedirect(reverse('user-profile',kwargs={'username':username}))
    





def StudentRegisterPage(request):
    return render(request, 'basic/register-student.html')


def StaffRegisterPage(request):
    return render(request, 'basic/register-staff.html')





def StudentRegister(request):
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
            user.studentuser.country = 'INDIA'
            user.save()
            messages.success(request, 'Registered User')
            return redirect('login-page')
        messages.error(request, "User already exists")    
        return redirect('register-page')
    messages.error(request, "Registeration cancelled")    
    return redirect('register-student-page')




def StaffRegister(request):
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
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
            user.staffuser.country = 'INDIA'
            user.save()
            user.staffuser.save()
            messages.success(request, 'Registered User')
            return redirect('login-page')
        messages.error(request, "User already exists")    
        return redirect('register-staff-page')
    messages.error(request, "Registration cancelled")    
    return redirect('register-staff-page')




def SelfPost(request):
    user_type = request.user.user_type
    if user_type == '1':
        return redirect('admin-self-post-list')
    if user_type == '2':
        return redirect('staff-self-post-list')
    if user_type == '3':
        return redirect('student-self-post-list')


def StudentList(request):
    user_type = request.user.user_type
    if user_type == '1':
        return redirect('admin-student-list')
    if user_type == '2':
        return redirect('staff-student-list')
    if user_type == '3':
        return redirect('student-student-list')
    

def StaffList(request):
    user_type = request.user.user_type
    if user_type == '1':
        return redirect('admin-staff-list')
    if user_type == '2':
        return redirect('staff-staff-list')
    if user_type == '3':
        return redirect('student-staff-list')
    

def ReportPage(request):
    return render(request, 'basic/reports.html')



def ReportSave(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    user = request.user
    reported_by = user.username if user.is_authenticated else 'Anonymous User'
    user_type = user.user_type if user.is_authenticated else 'AnonymousUser'
    report = Reports(title=title, description=description, reported_by=reported_by)
    try:
        file = request.FILES['file']
        file_store = FileSystemStorage()
        if user.is_authenticated:
            file_path = f'report/{user.user_type}/{user.id}/{file.name}'
        else:
            file_path = f'report/AnonymousUser/{file.name}'
        filename = file_store.save(file_path, file)
        file_url = file_store.url(filename)
        report.file = file_url
        report.save()
    except Exception:
        report.save()

    if user.is_authenticated:
        messages.success(request, 'Reported !')
        return HttpResponseRedirect(reverse('user-dashboard', kwargs={'username': user.username}))
    return HttpResponseRedirect(reverse('home-page'))

    







