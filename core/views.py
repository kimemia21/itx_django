from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Student,user
from .Serializers import StudentSeriailizer
from  django.contrib.auth.models import User


class StudentApiView(APIView):
    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
    def get(self ,request,pk=None,format=None):
        if pk:
            student =self.get_object(pk=pk)
            serializer =StudentSeriailizer(student,partial=True)
            return Response(serializer.data)
        else:
            student =Student.objects.all()
            serializer =StudentSeriailizer(student,many=True)
            return Response(serializer.data)
    
    def post(self,request):
        data =request.data
        serializer =StudentSeriailizer(data=data)
        if serializer.is_valid():
            serializer.save()    
            return Response({"sucess":serializer.data})
        else:
            return Response(serializer.errors)
    def put(self,request, pk=None,format=None):
        student =self.get_object(pk=pk)
        serializer =StudentSeriailizer(student,data =request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"user":serializer.data})
        else:
            return Response(serializer.errors,status=400)   
    def delete(self,request,pk,format=None):
        student =self.get_object(pk=pk)
        serializer =StudentSeriailizer(student,data=request.data,partial=True)
        if serializer.is_valid():
            student.delete()
            return Response({"message":"user deleted"})
        else:
            return Response(serializer.errors)     
        
        
 
class Login(APIView):
    def get(request):
        data =request.data
        try:
            User =user.objects.get(email=data.get("email"))
            
            
        
            
        except user.DoesNotExist:
            return Response({"not found":data["email"]}, Http404)
        
    
                 
        
        
        
        
        
        
        
        
        
                     


# Create your views here.
