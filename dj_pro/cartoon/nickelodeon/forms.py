from django import forms
from django.core.exceptions import ValidationError

from .models import CartoonUser


class CartoonUserForm(forms.ModelForm):
    username = forms.CharField(min_length=3, max_length=25)

    class Meta:
        model = CartoonUser
        fields = ['username', 'surname', 'email']

    def clean_username(self):
        data = self.cleaned_data['username']
        if len(data.split()) > 2:
            raise ValidationError('Amazing but invalid Username!')
        return data

    def clean_surname(self):
        data = self.cleaned_data['surname']
        if len(data.split()) > 2:
            raise ValidationError('Amazing but very long Surname')
        return data

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@ithillel.ua'):
            raise ValidationError('Wrong email-domain')
        else:
            return email

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        surname = cleaned_data.get('surname')
        if username and surname and (username in surname):
            raise ValidationError('Please start your login again')
