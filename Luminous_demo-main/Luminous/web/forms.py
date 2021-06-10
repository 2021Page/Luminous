from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    name = forms.CharField()
    phone = forms.CharField()
    address = forms.CharField()
    Choices = [('agree', 'agreement')]
    agreement = forms.CharField(label='agree', widget=forms.RadioSelect(choices=Choices))

    class Meta:
        model = User
        fields = ("username", "name", "phone", "address", "agreement")

class SearchForm(forms.Form):
    searchstr = forms.CharField(label='searchstr')