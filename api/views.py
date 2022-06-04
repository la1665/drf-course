from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import  IsAuthenticated
# from rest_framework.views import APIView
# from rest_framework.response import Response

from blog.models import Article
from .serializers import ArticleSerializer, Userserializer
from .permissions import IsSuperUser, IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffReadOnly


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


class UserList(ListCreateAPIView):
    def get_queryset(self):
        print(self.request.user)
        print(self.request.auth)  
        print("----------------")
        return User.objects.all()
    serializer_class = Userserializer
    permission_classes = (IsSuperUserOrStaffReadOnly, )


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes = (IsSuperUserOrStaffReadOnly, )

