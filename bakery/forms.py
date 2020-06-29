from django import forms 
from bakery.models import  contact,order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


	
		
class contactform(forms.ModelForm):
	name=forms.CharField(max_length=200)
	phone=forms.CharField(max_length=200)
	email=forms.CharField(max_length=200)
	message=forms.CharField(max_length=200)
	class Meta:
		model=contact
		fields="__all__"
		
	
	
class orderform(forms.ModelForm):
	name=forms.CharField(max_length=200)
	phone=forms.CharField(max_length=200)
	product=forms.CharField(max_length=200)
	email=forms.CharField(max_length=200)
	address=forms.CharField(max_length=200)
	class Meta:
		model=order
		fields="__all__"