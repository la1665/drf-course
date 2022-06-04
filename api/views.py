from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import  IsAuthenticated
from rest_framework.generics import RetrieveAPIView

from blog.models import Article
from .serializers import ArticleSerializer, Userserializer, AuthorSerializer
from .permissions import IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffReadOnly


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)
    filterset_fields = ['status', 'author', 'author__username']

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


class UserVIewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = Userserializer
    permission_classes = (IsSuperUserOrStaffReadOnly, )


class AuthorRetrive(RetrieveAPIView):
    queryset = get_user_model().objects.filter(is_staff=True)
    serializer_class = AuthorSerializer


