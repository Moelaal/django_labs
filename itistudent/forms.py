from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.forms import Form
from .models import students

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

class StudentForm(forms.ModelForm):
	class Meta:
		model = students
		fields = ("id", "name", "age","track")

class studForm(forms.Form):

    name=forms.CharField(max_length=40)
    age = forms.IntegerField()
    track = forms.CharField(max_length=20)
    class Meta:
        model = students
        fields = '__all__'


class studForm2(forms.ModelForm):

    name=forms.CharField(max_length=40)
    age = forms.IntegerField()
    track=forms.CharField(max_length=20)

    class Meta:
        model = students
        fields = '__all__'
        
           
