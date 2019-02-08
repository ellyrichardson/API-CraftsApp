from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from oauth2_provider.models import AbstractApplication

from .models import Posts

# variable for registering users
#UserModel = get_user_model()

# serializer for posts to be taken
class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id','post_title','post_content',)

    def create(self, validated_data):
        posts = Posts.objects.create(
            post_title=validated_data['post_title'],
            post_content=validated_data['post_content'],
            # gets the id of the current user
            post_user=self.context['request'].user.id, 
        )

        posts.save()
        return posts

# Serializer for user info for the registration API
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User # for the User model, use get_user_model for custom
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name',)
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('id',)

    # override create method
    def create(self, validated_data):
        if validated_data['client_id'] != "OI430uPmYGKUJ6h2C7Ohjdn2C9i3WONVMi7WQvu0" and validated_data['client_secret'] != "X8KJNUjIeXf7I8jIbzjt4k92rs6OPxSUqKv9IeaP6YRpLsK8YZVDLK8RcFDqacH4hKSzkuuZET42VyMkIltQt8mUwi16DCGwFWX3fJf7ZxcDMKA6wOQKJnX1GKh9bQ7a":
            raise serializers.ValidationError("Not allowed to do this MATE!")

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
            )

        user.set_password(validated_data['password'])
        user.save()

        return user
        



