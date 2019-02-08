# Views for the web page

#from django.shortcuts import render
from .models import Posts
from .serializers import PostsSerializer, UserSerializer
from rest_framework import generics, viewsets, permissions
from oauth2_provider.views.generic import ProtectedResourceView

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your views here.

# loads JWT settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# To retrieve and list all posts with DRF
class ListPosts(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # makes sure returns are only current user's post
    def get_queryset(self, *args, **kwargs):
        return Posts.objects.filter(post_user=self.request.user.id)

# To view the details of the listed posts with DRF
class DetailPosts(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class RegisterUserView(generics.CreateAPIView):
    model = User
    permission_classes = [permissions.AllowAny, ]
    serializer_class = UserSerializer
    queryset = ''

