from django import forms

from .models import *

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.Form):
    is_landlord = forms.BooleanField(label="Are you a landlord?", required=False)
    is_student = forms.BooleanField(label="Are you a student?", required=False)
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['address', 'photo', 'description', 'dishwasher', 'sublet', 'rent', 'move_in_date', 'lease_length', 'pets_allowed', 'num_beds', 'num_baths', 'num_sqr_ft']