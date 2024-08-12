from django.db import models


# class Movie(models.Model):
#     name =models.CharField(max_length=100)
#     director =models.TextField()
#     completed =models.BooleanField(default=True)
    
#     def __str__(self):
#         return self.name
    
class  Student(models.Model):
    first_name =models.CharField( max_length=100)
    last_name =models.CharField( max_length=100)   
    date_of_birth =models.DateField(auto_now=False, auto_now_add=False)
    grade =models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
    
    
    


# Create your models here.
