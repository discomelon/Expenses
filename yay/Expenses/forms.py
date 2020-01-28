from django import forms
from .models import *

class NadiaForm(forms.ModelForm):
    class Meta:
        model = Nadia
        fields = ('Title', 'Value', 'Category','Image', 'Description', 'Date')


class FarhanForm(forms.ModelForm):
    class Meta:
        model = Farhan
        fields = ('Title', 'Value', 'Category', 'Image', 'Description','Date')
        

class FarhanFamilySuperFundForm(forms.ModelForm):
    class Meta:
        model = FarhanFamilySuperFund
        fields = ('Title', 'Value', 'Category', 'Image', 'Description','Date')

class OngieForm(forms.ModelForm):
    class Meta:
        model = Ongie
        fields = ('Title', 'Value', 'Category', 'Image', 'Description','Date')

class OrangeTrust(forms.ModelForm):
    class Meta:
        model = OrangeTrust
        fields = ('Title', 'Value', 'Category', 'Image', 'Description','Date')






