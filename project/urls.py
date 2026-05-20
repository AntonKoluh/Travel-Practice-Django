from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import ProjectsViewSet

router = DefaultRouter()
router.register("", ProjectsViewSet, basename="project")

urlpatterns = [
    path("", include(router.urls)),
]
