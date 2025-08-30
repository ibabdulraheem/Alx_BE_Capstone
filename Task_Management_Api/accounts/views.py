from django.shortcuts import render
from rest_framework import generics,permissions
from django.contrib.auth.models import User
from .serializers import RegisterSerializer

# Create your views here.
#Registration View
class RegistrationView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer
  permission_classes = [permissions.AllowAny]

