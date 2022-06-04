from xml.etree.ElementInclude import include
from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "api"

router = routers.SimpleRouter()
router.register('articles', views.ArticleViewSet, basename='articles')
router.register('users', views.UserVIewSet, basename='users')

urlpatterns = [
    path("", include(router.urls)),
    path("authors/<int:pk>/", views.AuthorRetrive.as_view(), name="authors-detail")
]
