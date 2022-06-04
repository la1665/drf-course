from rest_framework import serializers

from django.contrib.auth import get_user_model
from blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'slug', 'author', 'content', 'publish', 'status')


class Userserializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = "__all__"
