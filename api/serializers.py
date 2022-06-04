from rest_framework import serializers

from django.contrib.auth import get_user_model
from blog.models import Article


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name"]


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedIdentityField(view_name='api:authors-detail')

    class Meta:
        model = Article
        fields = ('id', 'title', 'slug', 'author', 'content', 'publish', 'status')


class Userserializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = "__all__"
