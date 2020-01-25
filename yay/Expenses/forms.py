from django import forms
from .models import *

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptops
        fields = ('Title', 'Value', 'Category','Image', 'Description',)


class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktops
        fields = ('Title', 'Value', 'Category', 'Image', 'Description',)
        

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobiles
        fields = ('Title', 'Value', 'Category', 'Image', 'Description',)
