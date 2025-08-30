from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet,CategoryViewSet


router = DefaultRouter()
router.register(r'tasks',TaskViewSet,basename='tasks')
router.register(r'categories',CategoryViewSet,basename='categories')

urlpatterns = [
  path('',include(router.urls))
]
