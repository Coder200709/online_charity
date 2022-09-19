from django import forms
from django.contrib.auth import get_user_model

from django.core.exceptions import ValidationError

UserModel = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_confirm_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise ValidationError("Parollar bir xil emas!!!")
        return self.cleaned_data['confirm_password']

    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput()
        }
