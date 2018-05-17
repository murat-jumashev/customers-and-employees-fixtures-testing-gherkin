from django import forms
from authtools.forms import UserCreationForm

from .models import User


choices = (
    ('employee', 'Employee'),
    ('customer', 'Customer'),
)


class UserForm(UserCreationForm):
    type_of_user = forms.CharField(
        label="Type of user",
        widget=forms.RadioSelect(choices=choices)
    )
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2', 'type_of_user']
