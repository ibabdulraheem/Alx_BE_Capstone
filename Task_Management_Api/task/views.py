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
#Creating Task view 
class TaskViewSet(viewsets.ModelViewSet):
  serializer_class = TaskSerializer
  permission_classes = [permissions.IsAuthenticated,IsOwner] # user should be authenticated
  def get_queryset(self):
    Task.objects.filter(user = self.request.user) # Start with only the current user
#Filtering [STATUS, PRIORITY AND DUE_DATE]
    status_param = self.request.query_params.get('status')
    priority_param = self.request.query_params.get('priority')
    due_date_param = self.request.query_params.get('due_date')
    if status_param:
      queryset = queryset.filter(status = status_param)
    if priority_param:
      queryset = queryset.filter(status = priority_param)
    if due_date_param:
      queryset = queryset.filter(status = due_date_param)

#Sorting
    ordering = self.request.query_params.get('ordering')
    if ordering in ['due_date','-due_date','priority','-priority']:
      queryset = queryset.order_by(ordering)
      return queryset
  def perform_create(self, serializer):
    serializer.save(user = self.request.user)
    @action(detail=True,methods=['post'])
    def mark_complete(self,request,pk = None):
      task = self.get_object()
      if task.status == 'completed':
        return Response({'detail': 'Task already completed.'},status=status.HTTP_400_BAD_REQUEST)
      task.mark_complete()
      return Response(TaskSerializer(task).data,status=status.HTTP_200_OK)
    







  
