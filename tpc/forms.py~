from django import forms
from django.forms import ModelForm
from tpc.models import *

class RegisterationForm(ModelForm):
	class Meta:
		model=Drives
		fields = ['companyName','venue','description','skillsRequired','dateofdrive','branch']
		widgets = {
            		'companyName': forms.TextInput(attrs={'class': 'form-control '}),
        		'venue': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.TextInput(attrs={'class': 'form-control'}),
			'skillsRequired': forms.TextInput(attrs={'class':'form-control'}),
			'dateofdrive': forms.TextInput(attrs={'class':'form-control'}),
			'branch': forms.TextInput(attrs={'class':'form-control'}),
#'class': 'form-control'}),
			'time': forms.TextInput(attrs={'type':'hidden'}),#{'class': 'form-control'}),#,'disabled':''}),			
		}

class NoticeForm(ModelForm):
	class Meta:
		model=Notices
		fields = '__all__'
		widgets = {
			'time':forms.TextInput(attrs={'type':'hidden'}),
		}

class DriveRegisteration(ModelForm):
	class Meta:
		model=User
		fields = '__all__'
