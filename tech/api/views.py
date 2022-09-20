from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from tech.models import CustomUser, Posts, StaffUser, StudentUser
from . import serializers




@api_view(['GET'])
def PostsDetailViewAPI(request,id):
    try:
        post = Posts.objects.get(id=id)
    except post.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = serializers.PostsDetailViewSerializer(post)
    return Response(serializer.data)

@api_view(['GET'])
def AuthorDetails(request, id):
    try:
        user_obj = CustomUser.objects.get(id=id)
        serializer = serializers.AuthorDetailsSerializer(user_obj)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.data)



class SearchPostsListAPIView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = serializers.PostsDetailViewSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title','sub_title')



class SearchStudentListAPIView(ListAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = serializers.StudentListViewSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('college')


class SearchStaffListAPIView(ListAPIView):
    queryset = StaffUser.objects.all()
    serializer_class = serializers.StaffListViewSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('college')

    





























