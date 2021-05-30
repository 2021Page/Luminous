from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    name = forms.CharField()
    phone = forms.CharField()
    address = forms.CharField()

    class Meta:
        model = User
        fields = ("username", "name", "phone", "address")

class SearchForm(forms.Form):
    searchstr = forms.CharField(label='searchstr')