from django.db import models

# Create your models here.
class masterdpt(models.Model):
    dptname=models.CharField(max_length=100)
    dptcode=models.CharField(max_length=100)
    status=models.IntegerField(default=1)

class masterdesig(models.Model):
    designame=models.CharField(max_length=100)
    desigcode=models.CharField(max_length=100)
    status=models.IntegerField(default=1)

class masterqualif(models.Model):
    qualifname=models.CharField(max_length=100)
    status=models.IntegerField(default=1)

class masterclass(models.Model):
    classname=models.CharField(max_length=100)
    status=models.IntegerField(default=1)

class masterdivision(models.Model):
    divisionname=models.CharField(max_length=100)
    status=models.IntegerField(default=1) 

class masterempcat(models.Model):
    empcatname=models.CharField(max_length=100)
    empcatarea=models.IntegerField(default=0)
    status=models.IntegerField(default=1)
    
class subject(models.Model):
    sub_name=models.CharField(max_length=200)
    status=models.IntegerField(default=1)
    classes=models.ManyToManyField('masterclass')
    