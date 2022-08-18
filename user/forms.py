from django import forms
from .models import UserModel
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_confirm_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise ValidationError("Parollar bir xil emas!!!")
        return self.cleaned_data['confirm_password']

    class Meta:
        model = UserModel
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }
