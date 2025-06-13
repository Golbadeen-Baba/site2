from django import forms
from .models import TikTokProfile

class TikTokProfileForm(forms.ModelForm):
    class Meta:
        model = TikTokProfile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Your TikTok username'}),
            'video_types': forms.TextInput(attrs={'placeholder': 'e.g., funny, gaming, beauty'}),
            'followers_count': forms.NumberInput(attrs={'placeholder': 'Number of followers'}),
            'gets_engagement': forms.TextInput(attrs={'placeholder': 'Yes or No'}),  # No placeholder for checkbox

            'preferred_payment_method': forms.Select(attrs={'placeholder': 'Select preferred payment method'}),
            'preferred_currency': forms.TextInput(attrs={'placeholder': 'e.g., IDR, USD'}),

            'bank_account_name': forms.TextInput(attrs={'placeholder': 'Full name'}),
            'bank_name': forms.TextInput(attrs={'placeholder': 'bank name'}),
            'bank_account_number': forms.TextInput(attrs={'placeholder': 'account number'}),
            'bank_branch': forms.TextInput(attrs={'placeholder': 'e.g., Jakarta Barat'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Your phone number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'taxpayer_id': forms.TextInput(attrs={'placeholder': 'optional'}),
        }
