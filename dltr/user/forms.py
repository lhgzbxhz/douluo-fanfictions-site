from django import forms
from ckeditor.fields import RichTextFormField

from user.models import User


class UserForm(forms.ModelForm):
    uname = forms.CharField(max_length=20)
    password = forms.CharField(max_length=50)
    brief = RichTextFormField()

    class Meta:
        model = User
        fields = ['uname', 'password', 'brief']
