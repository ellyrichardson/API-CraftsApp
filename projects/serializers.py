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
        fields = ('id', 'post_title', 'post_content',)

    def create(self, validated_data):
        posts = Posts.objects.create(
            post_title=validated_data['post_title'],
            post_content=validated_data['post_content'],
            # gets the id of the current user
            post_user=self.context['request'].user.id,
        )

        posts.save()
        return posts


class SearchResultsSerializer(serializers.ModelSerializer):
    # Serializer for search results
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'id', 'email',)


class UserInfoSerializer(serializers.ModelSerializer):
    # Serializer for user info to get for profiles
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'id',)


class UserSerializer(serializers.ModelSerializer):
    # Serializer for user info for the registration API
    class Meta:
        model = User  # for the User model, use get_user_model for custom
        fields = ('username', 'password',
                  'email', 'first_name', 'last_name',)
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('id',)

    # override create method
    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
