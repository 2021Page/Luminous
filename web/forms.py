from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as django_user
from .models import *

class JoinForm(UserCreationForm):
    class Meta:
        model = django_user
        fields = ("username",)

class UserForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.CharField()
    phone = forms.CharField()
    city = forms.CharField() #address1
    gu = forms.CharField() #address2
    zipcode = forms.IntegerField()
    Choices = [('agree', 'agreement')]
    agreement = forms.CharField(label='agree', widget=forms.RadioSelect(choices=Choices))

    class Meta:
        model = User
        fields = ("name", "email", "phone", "city", "gu", "zipcode","agreement")


class SearchForm(forms.Form):
    searchstr = forms.CharField(label='searchstr')