from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

from tech.models import CustomUser, Posts, Reports, StaffUser, StudentUser
from tech.views import IllegalAccess, UserChecking








def AdminPublicProfile(request,username):
    user = CustomUser.objects.get(username=username)
    if user.user_type != '3':
        IllegalAccess(request)
    return render(request, 'portfolio/admin/public-profile.html',{'data':user})

def AdminPersonalProfile(request, username):
    UserChecking(request, username)
    return render(request, 'portfolio/admin/personal-profile.html')



def AdminProfileUpdate(request, username):
    if request.method != 'POST':
        IllegalAccess(request)
    UserChecking(request, username)

    user = CustomUser.objects.get(id=request.user.id)
    user.first_name = request.POST.get('firstname')
    user.last_name = request.POST.get('lastname')



    try:
        image = request.FILES['image']
        file = FileSystemStorage()
        file_path = f'profile/admin/{user.id}/{image.name}'
        filename = file.save(file_path, image)
        image_url = file.url(filename)
        user.adminuser.image = image_url
        
        user.save()
        user.adminuser.save()

        messages.success(request, 'Profile Updated with image !')
        return HttpResponseRedirect(reverse('user-dashboard',kwargs={'username':username}))

    except Exception:
        user.save()
        user.adminuser.save()
        messages.success(request,'Profile Updated without image !')
        return HttpResponseRedirect(reverse('user-dashboard',kwargs={'username':username}))



def AdminStudentList(request):
    student = StudentUser.objects.all()
    return render(request, 'portfolio/admin/students-list.html', {'data':student})


def AdminStaffList(request):
    staff = StaffUser.objects.all()
    return render(request, 'portfolio/admin/staffs-list.html', {'data':staff})

def AdminSelfPosts(request):
    post = Posts.objects.filter(created_by=request.user)

    return render(request, 'blog/admin/posts-list.html',{'data':post})


def ReportListView(request):
    data = Reports.objects.all()
    return render(request, 'Q&A/reports/report-list.html', {'data':data})



def ReportDetailView(request, id):
    data = Reports.objects.get(id=id)
    return render(request, 'Q&A/reports/report-detail-view.html', {'data':data})

















