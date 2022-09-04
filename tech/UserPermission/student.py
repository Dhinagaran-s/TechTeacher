from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

from tech.models import CustomUser, Posts, StudentUser, StaffUser
from tech.views import IllegalAccess, UserChecking






def StudentPublicProfile(request,username):
    user = CustomUser.objects.get(username=username)
    if user.user_type != '3':
        IllegalAccess(request)
    return render(request, 'portfolio/student/public-profile.html',{'data':user})

def StudentPersonalProfile(request, username):
    UserChecking(request, username)
    return render(request, 'portfolio/student/personal-profile.html')



def StudentProfileUpdate(request, username):
    if request.method != 'POST':
        IllegalAccess(request)
    UserChecking(request, username)

    user = CustomUser.objects.get(id=request.user.id)
    user.first_name = request.POST.get('firstname')
    user.last_name = request.POST.get('lastname')
    user.studentuser.about = request.POST.get('about')
    user.studentuser.college = request.POST.get('college')
    user.studentuser.interest = request.POST.get('interest')
    user.studentuser.country = request.POST.get('country')
    user.studentuser.department = request.POST.get('department')
    user.studentuser.address = request.POST.get('address')
    user.studentuser.portfolio = request.POST.get('portfolio')
    user.studentuser.projects = request.POST.get('projects')
    user.studentuser.internship = request.POST.get('internship')
    user.studentuser.position = request.POST.get('position')
    user.studentuser.phone_no = request.POST.get('phone')
    user.studentuser.twitter_profile = request.POST.get('twitter_profile')
    user.studentuser.facebook_profile = request.POST.get('facebook_profile')
    user.studentuser.instagram_profile = request.POST.get('instagram_profile')
    user.studentuser.linkedin_profile = request.POST.get('linkedin_profile')
    user.studentuser.github_profile = request.POST.get('github_profile')
    user.studentuser.kaggle_profile = request.POST.get('kaggle_profile')


    try:
        image = request.FILES['image']
        file = FileSystemStorage()
        file_path = f'profile/student/{user.id}/{image.name}'
        filename = file.save(file_path, image)
        image_url = file.url(filename)
        user.studentuser.image = image_url
        
        user.save()
        user.studentuser.save()

        messages.success(request, 'Profile Updated with image !')
        return HttpResponseRedirect(reverse('user-dashboard',kwargs={'username':username}))

    except Exception:
        user.save()
        user.studentuser.save()
        messages.success(request,'Profile Updated without image !')
        return HttpResponseRedirect(reverse('user-dashboard',kwargs={'username':username}))





def StudentStudentList(request):
    student = StudentUser.objects.all()
    return render(request, 'portfolio/student/students-list.html', {'data':student})


def StudentStaffList(request):
    staff = StaffUser.objects.all()
    return render(request, 'portfolio/student/staffs-list.html', {'data':staff})


def StudentSelfPosts(request):
    post = Posts.objects.filter(created_by=request.user)

    return render(request, 'blog/student/posts-list.html',{'data':post})





































