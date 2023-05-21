from django import forms
from django.core.exceptions import ValidationError

from .models import CartoonUser


class CartoonUserForm(forms.ModelForm):
    username = forms.CharField(min_length=3, max_length=25)
    class Meta:
        model = CartoonUser
        fields = ['username', 'surname']

    def clean_username(self):
        data = self.cleaned_data['username']
        if len(data.split()) > 2:
            raise ValidationError('Amazing but invalid Username!')
        return data

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        surname = cleaned_data.get('surname')
        if username and surname and (username not in surname):
            pass
        else:
            raise ValidationError('Please start your login form Username')
