"""qhacks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'leaf', LeafViewSet, basename='leaf')
router.register(r'recommendation', RecommendationViewSet, basename='recommendation')
router.register(r'userprofile', UserProfileViewSet, basename='userprofile')
router.register(r'crop', CropViewSet, basename='crop')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('csrf/', get_csrf_token, name='get-csrf-token')
]
