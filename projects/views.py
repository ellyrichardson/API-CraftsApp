# Views for the web page

#from django.shortcuts import render
from .models import Posts
from .serializers import PostsSerializer, UserSerializer, UserInfoSerializer, SearchResultsSerializer
from rest_framework import generics, viewsets, permissions
from oauth2_provider.views.generic import ProtectedResourceView

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from rest_framework import filters

# Create your views here.

# loads JWT settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class ListProfilePosts(generics.ListCreateAPIView):
    # To retrieve and list all posts of user signed in with DRF
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # makes sure returns are only current user's post
    def get_queryset(self, *args, **kwargs):
        return Posts.objects.filter(post_user=self.request.user.id)


class GetUserInfo(generics.ListCreateAPIView):
    # to retrieve user profile imfo
    queryset = ''
    serializer_class = UserInfoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # makes sure returns are only current user's info
    def get_queryset(self, *args, **kwargs):
        return User.objects.filter(id=self.request.user.id)


class SearchBoxResults(generics.ListAPIView):
    # to retrieve search box results
    queryset = User.objects.all()
    serializer_class = SearchResultsSerializer
    # using the searchFilter for searching users
    filter_backends = (filters.SearchFilter,)
    # can use search fields username and email for search
    search_fields = ('username', 'email', 'last_name', 'first_name',)
    permission_classes = (permissions.AllowAny,)


class ListHomePosts(generics.ListCreateAPIView):
    # Lists all posts in the app
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (permissions.AllowAny,)


class DetailPosts(generics.RetrieveUpdateDestroyAPIView):
    # To view the details of the listed posts with DRF
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (permissions.AllowAny,)


class RegisterUserView(generics.CreateAPIView):
    model = User
    permission_classes = [permissions.AllowAny, ]
    serializer_class = UserSerializer
    queryset = ''
