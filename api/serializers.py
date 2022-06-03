from rest_framework import serializers

from django.contrib.auth.models import User
from blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'slug', 'author', 'content', 'publish', 'status')


class Userserializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
