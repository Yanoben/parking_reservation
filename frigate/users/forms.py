from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Parking_place, MyUser


choice = (('Manager', 'Manager'), ('Employee', 'Employee'))


class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(
        required=True,
        choices=choice
    )
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                      'class': 'form-control',
                                      }))
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                      'class': 'form-control',
                                      }))
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username',
                                      'class': 'form-control',
                                      }))
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email',
                                      'class': 'form-control',
                                      }))
    password1 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                          'class': 'form-control',
                                          'data-toggle': 'password',
                                          'id': 'password',
                                          }))
    password2 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                          'class': 'form-control',
                                          'data-toggle': 'password',
                                          'id': 'password',
                                          }))

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name',
                  'username', 'email', 'role',
                  'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username',
                                      'class': 'form-control',
                                      }))
    password = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                          'class': 'form-control',
                                          'data-toggle': 'password',
                                          'id': 'password',
                                          'name': 'password',
                                          }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = MyUser
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = MyUser
        fields = ['username', 'email']


class CreateParkForm(forms.ModelForm):
    class Meta:
        model = Parking_place
        fields = ('owner', 'from_time', 'to_time', 'description')
        widgets = {
            'from_time': forms.TimeInput(format='%H:%M'),
            'to_time': forms.TimeInput(format='%H:%M'),
        }


class ChangeParkForm(forms.ModelForm):
    class Meta:
        model = Parking_place
        fields = ('owner', 'from_time', 'to_time', 'description')
