from django import forms
from django.forms.models import ModelForm
from django.utils.translation import ugettext_lazy as _

from mainapp.models import Deal


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )


class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}),
    )

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )

    password2 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
    )

    phone = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'placeholder': 'Phone number'})
    )


class DealForm(ModelForm):
    class Meta:
        model = Deal
        fields = ['name', 'description', 'total_price', 'number_of_items', 'ending_date', 'image']