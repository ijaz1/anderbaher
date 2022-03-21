from django.db import models


# Create your models here.


class contactUs(models.Model):
    phone = models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    whatsapp=models.CharField(max_length=10)

class category_images(models.Model):
    photo=models.ImageField(null=True)
    title=models.CharField(max_length=300)
    category=models.CharField(max_length=100)
    discription=models.CharField(max_length=1000,null=True)
    status=models.CharField(max_length=100)

class employerDetails(models.Model):
    first_Name=models.CharField(max_length=50)
    last_Name=models.CharField(max_length=50)
    job_Title=models.CharField(max_length=100)
    title_Position=models.CharField(max_length=50)
    personal_Email=models.CharField(max_length=100)
    phone_Number=models.CharField(max_length=12)
    address=models.CharField(max_length=1000)
    gender=models.CharField(max_length=10)
    account_Holder_Name=models.CharField(max_length=100)
    bank_Name=models.CharField(max_length=100)
    branch_Name=models.CharField(max_length=100)
    account_Number=models.CharField(max_length=500)
    IFSC_Code=models.CharField(max_length=100)
    signIn_Email=models.CharField(max_length=100)
    signIn_Password=models.CharField(max_length=10,null=True)
    status=models.CharField(max_length=20,null=True)
    photo=models.ImageField(upload_to='employees_photo' ,null=True)
    id_proof=models.ImageField(upload_to='employee_id_proof',null=True)
    date_of_birth=models.DateField(null=True)

class WorkAssign(models.Model):
    employer=models.ForeignKey(employerDetails,on_delete=models.CASCADE)
    task=models.CharField(max_length=500,null=True)
    starting_date=models.CharField(max_length=50)
    ending_date=models.CharField(max_length=50)
    starting_time=models.CharField(max_length=50)
    ending_time=models.CharField(max_length=50)
    client_First_name=models.CharField(max_length=100)
    Client_second_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=50)
    street_address=models.CharField(max_length=500)
    city=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    additional_information=models.CharField(max_length=3000)
    work_status=models.CharField(max_length=100,null=True)