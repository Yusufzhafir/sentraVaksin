from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=100)
    username = forms.CharField(required=True, max_length=25)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True, max_length=25)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, max_length=25)
    
    class Meta:
    	model = User
    	fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
    	user = super(NewUserForm, self).save(commit=False)
    	user.email = self.cleaned_data['email']
    	if commit:
    		user.save()
    	return user
    
    