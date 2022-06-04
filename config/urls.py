from django import views
from django.contrib import admin
from django.urls import path, include
# from rest_framework.authtoken import views as token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('api/', include('api.urls')),
    # path('api/auth/', token.obtain_auth_token),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    
]
