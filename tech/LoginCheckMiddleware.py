from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, path, include
from django.utils.deprecation import MiddlewareMixin





class LoginCheckMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user



        if user.is_authenticated:
            if user.user_type == '1':
                if modulename in ['tech.UserPermission.admin', 'tech.views', 'django.views.static']:
                    pass
            elif user.user_type == '2':
                if modulename in ['tech.UserPermission.staff', 'tech.views', 'django.views.static']:
                    pass
            elif user.user_type == '3':
                if modulename in ['tech.UserPermission.student', 'tech.views', 'django.views.static']:
                    pass
        else:
            if modulename in ['tech.views', 'django.views.static']:
                pass
            else:
                return redirect('home-page')



