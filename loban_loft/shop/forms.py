from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.forms import ModelForm, TextInput, Textarea

from django.utils.translation import gettext as _
from .models import Reviews, Application


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'name': 'password1',
                'placeholder': 'Enter Password'
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'name': 'password1',
                'placeholder': 'Re-Enter Password'
            }
        ),
        strip=False,
        help_text=_("Enter the same password as before, for verification.")
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'name': 'password1',
                'placeholder': 'Enter Username'
            }
        )
    )
    # email = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'name': 'email',
    #             'placeholder': 'Enter Email'
    #         }
    #     )
    # )


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'name': 'password1',
                'placeholder': 'Enter Login'
            }
        )
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'name': 'password1',
                'placeholder': 'Enter Password'
            }
        ),
    )


class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ('name', 'text')


class ApplicationModelForm(ModelForm):
    class Meta:
        model = Application
        fields = ('name', 'number', 'message', 'slug')
        widgets = {
            'name': TextInput(
                attrs={'class': 'form-control', 'id': 'Name', 'placeholder': 'Введите имя'}
            ),
            'number': TextInput(
                attrs={'class': 'form-control', 'id': 'Number', 'placeholder': 'Введите номер'}
            ),
            'message': Textarea(
                attrs={'class': 'form-control', 'id': 'Message', 'placeholder': 'Введите сообщение'}
            ),
            'slug': TextInput(
                attrs={'reqired': False, 'hedden': 'True', 'id': 'slug', 'value': ' '}
            )
        }
