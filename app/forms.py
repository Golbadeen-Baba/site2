from django import forms
from django_flatpickr.widgets import DatePickerInput
from .models import ModelQuestionnaire

class ModelApplicantForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Phone number',
        })
    )
    date_of_birth = forms.DateField(widget=DatePickerInput(attrs={'placeholder': 'DoB (YYYY-MM-DD)', 'data-input': True, 'data-alt-input': True, 'data-alt-format': 'F j, Y', 'data-date-format': 'Y-m-d'}))
    instagram_handle = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Instagram handle'}))


