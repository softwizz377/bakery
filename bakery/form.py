from django import forms 
from app1.models import category,products
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class categoryform(forms.ModelForm):
	name=forms.CharField(max_length=200)
	picimage=forms.CharField(max_length=200)
	class Meta:
		model=category
		fields="__all__"
	
	
class productform(forms.ModelForm):
	name=forms.CharField(max_length=200)
	category=forms.CharField(max_length=200)
	picimage=forms.CharField(max_length=200)
	price=forms.CharField(max_length=200)
	class Meta:
		model=products
		fields="__all__"
		
		
class SignForm(UserCreationForm):
	class Meta:
		model=User
		fields=('first_name','last_name','email','username','password1','password2')