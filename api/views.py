from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from django.contrib.auth.models import User
from .serializers import ArticleSerializer, Userserializer
from blog.models import Article


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer

