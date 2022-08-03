from django.db import models

# Create your models here.

class District(models.Model):
    districtName = models.CharField(max_length=50,blank=True,null=True)
    createdDate=models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.id

class Taluka(models.Model):
    talukaName=models.CharField(max_length=255)
    createdDate=models.DateTimeField(auto_now_add=True)
    district=models.ForeignKey(District,on_delete=models.CASCADE,blank=True,null=True,related_name = 'district')
    def __unicode__(self):
        return self.id
    


class Application(models.Model):
    name = models.CharField(max_length=500,blank=True,null=True)
    aadharNumber = models.CharField(max_length=25,blank=True,null=True)
    phoneNumber = models.CharField(max_length=15,blank=True,null=True)
    district = models.CharField(max_length=100,blank=True,null=True)
    taluka = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=300,blank=True,null=True)
    haveGasConnection = models.BooleanField(default=False)
    belongToSC = models.BooleanField(default=False)
    createdDate=models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.id
    