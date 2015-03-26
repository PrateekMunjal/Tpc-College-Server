from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=100)
	stream = models.CharField(max_length=20)
	cgpa = models.CharField(max_length=100)
	roll_no = models.CharField(max_length=30)
	contact = models.CharField(max_length=100)	
        company_reg = models.CharField(max_length=100)

class Drives(models.Model):
	companyName = models.CharField(max_length=1000)
	venue = models.CharField(max_length=1000)
	description = models.CharField(max_length=4000)
	skillsRequired = models.CharField(max_length=2000,default='Non Specified By Company')
	branch = models.CharField(max_length=200)
	dateofdrive = models.CharField(max_length=300)
	time = models.DateTimeField('date published',default=timezone.now)

class Notices(models.Model):
	heading = models.CharField(max_length=10000)
	message = models.TextField(max_length=10000)
	time = models.DateTimeField('date published',default=timezone.now)
	
