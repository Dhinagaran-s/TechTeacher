from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


from tech.models import CustomUser, Posts, StudentUser, StaffUser
from tech.views import IllegalAccess, UserChecking








def StaffPublicProfile(request, username):
    user = CustomUser.objects.get(username=username)
    if user.user_type != '1':
        IllegalAccess(request)
    return render(request, 'portfolio/staff/public-profile.html',{'data':user})




def StaffPersonalProfile(request, username):
    UserChecking(request, username)
    return render(request, 'portfolio/staff/personal-profile.html')




def StaffProfileUpdate(request, username):
    if request.method != 'POST':
        IllegalAccess(request)
    UserChecking(request, username)

    user = CustomUser.objects.get(id=request.user.id)
    user.first_name = request.POST.get('firstname')
    user.last_name = request.POST.get('lastname')
    user.staffuser.department = request.POST.get('department')
    user.staffuser.portfolio = request.POST.get('portfolio')
    user.staffuser.college = request.POST.get('college')
    user.staffuser.interest = request.POST.get('interest')
    user.staffuser.country = request.POST.get('country')
    user.staffuser.address = request.POST.get('address')
    user.staffuser.phone_no = request.POST.get('phone')
    user.staffuser.about = request.POST.get('about')
    user.staffuser.experiance = request.POST.get('experiance')
    user.staffuser.facebook_profile = request.POST.get('facebook_profile')
    user.staffuser.instagram_profile = request.POST.get('instagram_profile')
    user.staffuser.linkedin_profile = request.POST.get('linkedin_profile')
    user.staffuser.twitter_profile = request.POST.get('twitter_profile')
    user.staffuser.github_profile = request.POST.get('github_profile')
    user.staffuser.kaggle_profile = request.POST.get('kaggle_profile')
    user.staffuser.mentor = request.POST.get('mentor')
    user.staffuser.position = request.POST.get('position')

    try:
        image = request.FILES['image']
        file = FileSystemStorage()
        file_path = f'profile/staff/{user.id}/{image.name}'
        filename = file.save(file_path, image)
        image_url = file.url(filename)
        user.staffuser.image = image_url
        
        user.save()
        user.staffuser.save()

        messages.success(request, 'Profile Updated with image !')
        return HttpResponseRedirect(reverse('user-dashboard',kwargs={'username':username}))

    except Exception:
        user.save()
        user.staffuser.save()
        messages.success(request,'Profile Updated without image !')
        return HttpResponseRedirect(reverse('user-dashboard',kwargs={'username':username}))




def StaffStudentList(request):
    student = StudentUser.objects.all()
    return render(request, 'portfolio/staff/students-list.html', {'data':student})


def StaffStaffList(request):
    staff = StaffUser.objects.all()
    return render(request, 'portfolio/staff/staffs-list.html', {'data':staff})


def StaffSelfPosts(request):
    post = Posts.objects.filter(created_by=request.user)

    return render(request, 'blog/staff/posts-list.html',{'data':post})



















