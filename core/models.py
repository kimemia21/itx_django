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
        

class users(models.Model):
    selections =[('buyer',"Buyer"),('seller',"Seller"),('producer',"Producer"),]
    email =models.EmailField(max_length=254),
    password =models.CharField(max_length=100),
    c2fc =models.CharField(max_length=8),
    phone_number =models.CharField(max_length=50),
    role =models.CharField(choices=selections,max_length=50,default="buyer")
     
    def __str__(self):
        return self.email

   


# Create your models here.
