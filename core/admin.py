from django.contrib import admin
from .models import Student,user

# Register your models here.
admin.site.register([Student,user])