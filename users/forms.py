from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

from users.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры.')
        return phone

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class':'form-control', 'placeholder':'Email'})
        #self.fields['password'].widget.attrs.update({'class':'form-control', 'placeholder':'Password'})
        self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder':'Password confirm'})
        #self.fields['phone'].widget.attrs.update({'class':'form-control', 'placeholder':'Phone'})
    #     self.fields['text'].widget.attrs.update({'class':'form-control', 'placeholder':'Text of post'})

class CustomAuthenticationForm(AuthenticationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'password']
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Email'})
        self.fields['password'].widget.attrs.update({'class':'form-control', 'placeholder':'Password'})

class CabinetForm(PasswordChangeForm):
    """Cabinet post form"""
    class Meta:
        model = User
        #fields = ['phone', 'password']

    def __init__(self, *args, **kwargs):
        super(CabinetForm, self).__init__(*args, **kwargs)
        #self.fields['phone'].widget.attrs.update({'class':'form-control', 'placeholder':'Header of post'})
        self.fields['old_password'].widget.attrs.update({'class':'form-control', 'placeholder':'Old pass'})
        self.fields['new_password1'].widget.attrs.update({'class':'form-control', 'placeholder':'Text of post'})
        self.fields['new_password2'].widget.attrs.update({'class':'form-control', 'placeholder':'Text of post'})


class PasswordRestoreForm(forms.Form):
    email = forms.CharField(max_length=100, label='Your email')