from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
from datetime import date


# Create your models here.


class CustomUser(AbstractUser):
    user_type_choices = ((1,'Admin'),(2,'Staff'),(3,'Student'))
    user_type = models.CharField(default=1, max_length=20, choices=user_type_choices)



class AdminUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.PROTECT, default='')
    image = models.ImageField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class StaffUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.PROTECT, default='')
    department = models.CharField(max_length=50, blank=True, default='')
    college = models.CharField(max_length=100, blank=True, default='')
    interest = models.CharField(max_length=50, blank=True, default='')
    country = models.CharField(max_length=30, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    phone_no = models.IntegerField(default=0, blank=True) 
    about = models.TextField(blank=True, default='')
    cv = models.FileField(blank=True)
    experiance = models.IntegerField(default=0, blank=True)
    posts = models.IntegerField(default=0, blank=True)
    facebook_profile = models.URLField(blank=True)
    instagram_profile = models.URLField(blank=True)
    linkedin_profile = models.URLField(blank=True)
    twitter_profile = models.URLField(blank=True)
    github_profile = models.URLField(blank=True)
    kaggle_profile = models.URLField(blank=True)
    portfolio = models.URLField(default='')
    image = models.ImageField(blank=True)
    mentor = models.IntegerField(default=0, blank=True)
    position = models.CharField(max_length=100, default='', blank=True)
    is_permanent = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()



class StudentUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.PROTECT, default='')
    about = models.TextField(blank=True)
    department = models.CharField(max_length=50, blank=True, default='')
    college = models.CharField(max_length=100, default='', blank=True)
    interest = models.CharField(max_length=30, default='', blank=True)
    country = models.CharField(max_length=20, default='India', blank=True)
    address = models.CharField(max_length=100, default='', blank=True)
    phone_no = models.IntegerField(default=0, blank=True)
    email = models.EmailField(blank=True)
    facebook_profile = models.URLField(blank=True)
    instagram_profile = models.URLField(blank=True)
    linkedin_profile = models.URLField(blank=True)
    twitter_profile = models.URLField(blank=True)
    github_profile = models.URLField(blank=True)
    kaggle_profile = models.URLField(blank=True)
    portfolio = models.URLField(default='', blank=True)
    projects = models.IntegerField(default=0, blank=True)
    internship = models.IntegerField(default=0, blank=True)
    posts = models.IntegerField(default=0, blank=True)
    resume = models.FileField(blank=True)
    image = models.ImageField(blank=True)
    position = models.CharField(max_length=100, default='', blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()



class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80, blank=False)
    sub_title = models.CharField(max_length=50, blank=True, default='')
    body = RichTextField(default='')
    created_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Posts'

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=15, blank=False, default='')
    created_by = models.CharField(max_length=50, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.tag_name


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, default='')
    comment = RichTextField(default='')
    commented_by = models.CharField(max_length=50, default='', blank=True)
    commented_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.post.title



class Reports(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default='', blank=True)
    description = models.TextField(default='', blank=True)
    file = models.FileField(blank=True)
    reported_at = models.DateTimeField(auto_now_add=True)
    reported_by = models.CharField(max_length=100, default='', blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Reports'










@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    # sourcery skip: instance-method-first-arg-name
    if not created:
        return
    if instance.user_type==1:
        AdminUser.objects.create(admin=instance)
    if instance.user_type == 2:
        StaffUser.objects.create(admin=instance)
    if instance.user_type == 3:
        StudentUser.objects.create(admin=instance)
    


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminuser.save()
    if instance.user_type == 2:
        instance.staffuser.save()
    if instance.user_type == 3:
        instance.studentuser.save()


































