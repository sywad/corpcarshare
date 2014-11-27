from django import forms

from .models import eachpost, eachcompany
from django.forms.extras.widgets import SelectDateWidget


class eachpostform(forms.ModelForm):
	email = forms.EmailField(required = True, max_length=70, widget=forms.TextInput(attrs={ 'placeholder': ' corporate email required', 'class': 'form-control'}))
	homezip = forms.CharField(required = True, max_length = 5, widget=forms.TextInput(attrs={'class': 'form-control' }))
	workname = forms.CharField(required = True, max_length = 30, widget=forms.TextInput(attrs={'placeholder': ' your company name', 'class': 'form-control' }))
	workaddr = forms.CharField(required = True, max_length = 50, widget=forms.TextInput(attrs={'placeholder': ' your company address', 'class': 'form-control' }))
	workzip = forms.CharField(required = True, max_length = 5, widget=forms.TextInput(attrs={'class': 'form-control' }))
	class Meta:
		model = eachpost


class eachcompanyform(forms.ModelForm):
	compname = forms.CharField(required = True, max_length = 30)
	compzip = forms.CharField(required = True, max_length = 5)
	compaddr = forms.CharField(required = True, max_length = 50)
	
	class Meta:
		model = eachcompany