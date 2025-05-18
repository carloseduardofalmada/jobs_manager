from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address', 'is_account_customer']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }