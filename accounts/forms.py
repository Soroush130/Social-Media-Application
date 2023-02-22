from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'username')


class RegisterForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    re_password = forms.CharField(widget=forms.PasswordInput())

    def clean_email(self) -> str:
        email = self.cleaned_data['email']
        is_exists_email = User.objects.filter(email=email).exists()
        if is_exists_email:
            raise forms.ValidationError('Such an email has already been registered')
        return email

    def clean_re_password(self) -> str:
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']

        if password != re_password:
            raise forms.ValidationError("The passwords are different")

        return password

    def clean_username(self) -> str:
        username = self.cleaned_data['username']
        is_exists_email = User.objects.filter(username=username).exists()
        if is_exists_email:
            raise forms.ValidationError('Such an username has already been registered')

        return username


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
