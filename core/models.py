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
        

class user(models.Model):
    # selections =[('buyer',"Buyer"),('seller',"Seller"),('producer',"Producer")]
   
      
    email =models.EmailField(max_length=255,null=True,default="test")
    password =models.CharField(max_length=100,null=True,default="test")
    c2fc =models.CharField(max_length=8,null=True,default="test")
    # phone_number =models.CharField(max_length=20,null=True,default="test")
    # role =models.CharField(max_length=50,default="seller")
     
    def __str__(self):
        return self.email
 
class commodites(models.Model):
    id =models.IntegerField(max_length=255, primary_key=True)
    name  =models.CharField( max_length=255)
    commodity_type ="Foreign key from commodites_type"
    description=models.TextField()
    icon_name =models.CharField(max_length=100)
    image_url =models.CharField( max_length=255)
    commodity_primary_packing_id =  id
 
    
class user_has_commodity(models.Model):
    user_id =models.ForeignKey(user, verbose_name=_(""), on_delete=models.CASCADE)    
    commodity_id =models.ForeignKey(commodites , on_delete=models.CASCADE)
    user_has_commodity_id =models.IntegerField(primary_key=True,max_length=11)
    
    
class jurisdictions(models.Model):
    jurisdictions_name =models.CharField( max_length=100)
    description=models.TextField()
   
    

class banking_profile(models.Model):
    user_id= models.ForeignKey(user, on_delete=models.CASCADE)
    banking_profile_id =models.IntegerField(max_length=11,primary_key=True)
    bank_branch_id=models.CharField( max_length=10)
    swift =models.CharField( max_length=30)
    IBAN =models.CharField( max_length=100)
    
class user_has_usertype(models.Model):
    usertypeid ="foreignkey from usertypes"
    user_id =models.ForeignKey(user , on_delete=models.CASCADE)
    
        
    
    
class sale_packaging(models.Model):
    packing_id =models.ForeignKey(jurisdictions, on_delete=models.CASCADE)
    packing_name =models.CharField( max_length=100)
    commodites_id=models.ForeignKey(commodites, verbose_name=_(""), on_delete=models.CASCADE) 
    

 
class countries(models.Model):
    name =models.CharField( max_length=100)
        
    
class country_is_within_jurisdiction(models.Model):
    
        
           
    
    
    
    
        
    
    
# class user_has_usertype(models.Model):
#     usertypeid =models.ForeignKey("model.user", on_delete=models.CASCADE) 
        
    
    

   

# Create your models here.

