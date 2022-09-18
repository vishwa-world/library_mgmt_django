from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from importlib import import_module
from .models import Book
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'aitofocus': True,
        'class': 'form-control',
    }))

    password = forms.CharField(label=("Password"), strip=False,
                               widget=forms.PasswordInput(attrs={
                                   'autocomplete': 'current-password',
                                   'class': 'form-control',
                               }))


class SignupForm(UserCreationForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                'class':'form-control'
            }), label='Confirm Password ')

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
                'class':'form-control'
            }), label='Password ')
            
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email']
        labels = {
            'first_name': 'Name ',
            'username': 'User Name ',
            'email': 'Email ',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Username'
            }),

            'first_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'First Name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'name@example.com'
            })
        }


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'pubDate']
        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'pubDate': 'Publisher Date'
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'author': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'pubDate': forms.DateInput(
                attrs={
                    'class': 'form-control' , 'placeholder': 'YYYY-MM-DD'
                }
            ),
        }


class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'pubDate']
        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'pubDate': 'Publisher Date'
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'author': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'pubDate': forms.DateInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'YYYY-MM-DD'
                }
            ),
        }
