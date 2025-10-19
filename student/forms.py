from django import forms
from . import models

class studentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model  = models.student
        fields = '__all__'
        labels = {
            'name' : "Full Name",
            'photo':"Upload Photo",
            'unique_ID': "Student ID"
        }
        help_texts ={
            'email' : "Enter your valid email address",
            'password' : "Minimum 4 characters ",
            'unique_ID': "Enter a unique student ID"
        }
       