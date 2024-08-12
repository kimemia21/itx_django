from rest_framework import serializers
from .models import Student,user

class StudentSeriailizer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields ="__all__"
        

class usererializer(serializers.ModelSerializer):
    class Meta:
        model =user
        fields="_all__"       