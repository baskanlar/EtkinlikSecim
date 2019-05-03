from django import forms
from django.contrib.auth import authenticate
from User.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Parola')

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise forms.ValidationError('Kullanıcı Adını veya Paraloyı yanlış girdiniz!')
        return super(LoginForm, self).clean()


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Email')
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Parola')
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Parola Doğrulama')

    class Meta:
        model = User
        fields = [
            'email',
            'password1',
            'password2',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Parolalar Eşleşmiyor')
