from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



#creating serializer for user Registration
class RegisterSerializer(serializers.ModelSerializer):
  class meta:
    model = User
    fields = ['id','username','email','password']
    extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
      validated_data['password'] = make_password(validated_data['password'])
      return User.objects.create(**validated_data)