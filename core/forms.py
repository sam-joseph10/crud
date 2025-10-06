from django import forms
from .models import student

class AddstudentForm(forms.ModelForm):

    class Meta:
        model = student
        fields = ("name","roll",'city')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'roll':forms.NumberInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
        }
     