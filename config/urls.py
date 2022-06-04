from django import views
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('api/', include('api.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/rest-auth/', include('dj_rest_auth.urls')),
    # path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    
]
