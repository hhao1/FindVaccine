from djongo import models


class Lead(models.Model):
    Country_Name=models.CharField(max_length=100)
    Vaccine=models.CharField(max_length=100,blank=True)
    #email=models.EmailField(max_length=100,unique=True)
    message=models.CharField(max_length=500,blank=True)#optional

# Create your models here.
