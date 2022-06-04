from xml.etree.ElementInclude import include
from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "api"

router = routers.SimpleRouter()
router.register('', views.ArticleViewSet, basename='Article')
router.register('users', views.UserVIewSet, basename='User')

urlpatterns = [
    path("", include(router.urls)),

]
