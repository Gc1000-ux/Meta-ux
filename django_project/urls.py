from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework import routers

from LittleLemon import views

router = routers.DefaultRouter()
router.register(r'tables', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('littlelemon/', include('LittleLemon.urls')),
    path('littlelemon/menu/', include('LittleLemon.urls')),
    path('littlelemon/booking/', include(router.urls)),
    path('api/', include('LittleLemon.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
