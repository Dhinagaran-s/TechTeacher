from rest_framework import serializers
from tech.models import CustomUser, Posts, StaffUser, StudentUser




class PostsDetailViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id','title','sub_title','body','created_by','created_at']

class AuthorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username']




class StudentListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = ['projects','college','posts']

class StudentListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = ['about','department','college','interest','country','email','facebook_profile','instagram_profile','linkedin_profile','twitter_profile','github_profile','kaggle_profile','portfolio','internship','posts','position']


class StaffListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffUser
        fields = ['mentor','college','posts']


class StaffDetailViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffUser
        fields = ['department','college','interest','country','about','experiance','posts','facebook_profile','instagram_profile','linkedin_profile','twitter_profile','github_profile','kaggle_profile','portfolio','mentor','position']
















