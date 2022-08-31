from django.contrib import admin

from tech.models import AdminUser, Posts, StaffUser, StudentUser

# Register your models here.







admin.site.register(Posts)
admin.site.register(AdminUser)
admin.site.register(StaffUser)
admin.site.register(StudentUser)


