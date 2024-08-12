from rest_framework import serializers
from .models import Student,users

class StudentSeriailizer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields ="__all__"
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =users
        fields="_all__"       