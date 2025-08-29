from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

# creating Category model (Organizes tasks into 'Work' and 'Personal')
class Category (models.Model):
  name = models.CharField(max_length=100)
  user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='categories')
  def __str__(self):
    return self.name
  
#Creating Task model
class Task (models.Model):
  PRIORITY_CHOICES = [
    ('low','Low'),
    ('medium','Medium'),
    ('high','High')
  ]

  STATUS_CHOICES = [
    ('pending','Pending'),
    ('completed','Completed')
  ]
  title = models.CharField(max_length=250)
  description = models.TextField(blank=True)
  due_date = models.DateField(null=True,blank=True)
  priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
  status = models.CharField(max_length=10, choices= STATUS_CHOICES, default='pending')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
  category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
#Method that marks task as complete
  def mark_complete(self):
    self.status = 'completed'
    self.completed_at = timezone.now()
    self.save()

#Method that marks task as incomplete
  def mark_incomplete(self):
    self.status = 'pending'
    self.completed_at = None
    self.save()
#Check if a task is editable or not (Returns only non completed tasks)
  def editable_task(self):
    return self.status != 'completed'
  def __str__(self):
    return f'{self.title} ({self.status})'

