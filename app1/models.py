from django.db import models

# Create your models here.

class get_an_estimate(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    villa_apartment_property=models.CharField(max_length=1000)
    city_zip=models.CharField(max_length=300)
    estimated_budget=models.CharField(max_length=200)
    when_to_start_work=models.CharField(max_length=200) 
    checkout=models.CharField(max_length=20,null=True)   

class signUp(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=10)
    what_are_you_looking_for=models.CharField(max_length=20)