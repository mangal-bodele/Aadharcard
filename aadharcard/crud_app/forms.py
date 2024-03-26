from django import forms
from .models import AadharCard

class AadharCardForm(forms.ModelForm):
    class Meta:
        model = AadharCard
        fields = '__all__'

        widgets = {
            'fname': forms.TextInput(attrs={'class':'form-control'}),
            'lname': forms.TextInput(attrs={'class':'form-control'}),
            'mobile_number': forms.NumberInput(attrs={'class':'form-control'}),
            'aadhar': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.NumberInput(attrs={'type':'date','class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'})
        }
        labels={
            'dob':"Date Of Birth",
            'aadhar':'AadharCard No.',
            'fname':'First Name',
            'lname':'Last Name'
        }