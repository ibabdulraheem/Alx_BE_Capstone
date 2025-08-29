from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task, Category
from .serializers import TaskSerializer,CategorySerializer

# Create your views here.

#Allows only the owner to access their tasks
class IsOwner(permissions.BasePermission):

  def has_object_permission(self, request, view, obj):
    return obj.user ==  request.user
# User must login   
class CategoryViewSet(viewsets.ModelViewSet):
  serializer_class = CategorySerializer
  permission_classes = [permissions.IsAuthenticated]
#method to list all categories
  def get_category(self):
    Category.objects.filter(user = self.request.user)

  def perform_create(self, serializer):
    serializer.save(user = self.request.user)

