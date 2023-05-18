from django import forms
from django.core.exceptions import ValidationError


class CartoonUserForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=20)
    surname = forms.CharField(min_length=3, max_length=20)

    def clean_username(self):
        data = self.cleaned_data['username']
        if len(data.split()) > 2:
            raise ValidationError('Amazing but invalid Username!')
        return data
