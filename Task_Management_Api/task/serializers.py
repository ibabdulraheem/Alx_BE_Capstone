from rest_framework import serializers
from .models import Task,Category

#Creating serializer for category model
class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id','name']

#Creating serializer for Task model
class TaskSerializer(serializers.ModelSerializer):
  user = serializers.ReadOnlyField(source = 'user.username')
  category = CategorySerializer(read_only = True)
  category_id = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all(),source = 'Category',write_only = True,required = False)
  class Meta:
    model = Task
    fields = ['id','user','title','description','due_date','priority','status','category','category_id']
    read_only_field = ['status','completed_at']
#Editting is restricted if task is completed
    def validate(self,data):
      if self.instance and self.instance.status == 'completed':
        raise serializers.ValidationError('Completed task cannot be edited!')
      return data
