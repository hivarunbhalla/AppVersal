
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('api', views.appViewSet, basename='app')

urlpatterns = [
    # path('', views.home),
    path('', views.home),
    
] + router.urls
