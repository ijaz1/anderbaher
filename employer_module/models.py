from django.db import models
from admin_module.models import employerDetails

# Create your models here.
class workStatus(models.Model):
    employer=models.ForeignKey(employerDetails,on_delete=models.CASCADE)
    current_date=models.DateField()
    current_time=models.TimeField()
    end_time=models.TimeField()
    ended_time=models.TimeField(default='0:0:0')