from django.urls import path
from . import views


app_name = "api"

urlpatterns = [
    path('', views.ArticleList.as_view(), name="list"),
    path('<int:pk>/', views.ArticleDetail.as_view(), name="detail"),
    path('users/', views.UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
    # path('revoke/', views.RevokeToken.as_view()),

]
