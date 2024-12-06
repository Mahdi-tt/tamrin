from django import forms
from .models import contact
from django.forms import ModelForm

# create forms 

class contactForm(forms.ModelForm):
      
    class Meta():
        model = contact
        fields = ['email'] 