from django import forms
from django.forms.widgets import ClearableFileInput
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
    
"""class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['address', 'description', 'dishwasher', 'sublet', 'rent', 'move_in_date', 'lease_length', 'pets_allowed', 'num_beds', 'num_baths', 'num_sqr_ft']
    photo = forms.ImageField(label='Photo')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].required = False"""
        
class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['address', 'description', 'dishwasher', 'sublet', 'rent', 'move_in_date', 'lease_length', 'pets_allowed', 'num_beds', 'num_baths', 'num_sqr_ft']

class PhotoForm(forms.Form):
    photos = MultipleFileField(required=False)
        
class MessageForm(forms.Form):
    class Meta:
        model = Message
        fields = ['recipient', 'content']