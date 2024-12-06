from.models import comment
from django import forms


class commentforms(forms.ModelForm):  
    class Meta():
        model = comment
        exclude = ('approved',)