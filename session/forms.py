from django import forms
from User.models import User

class login(forms.ModelForm):
    email = forms.EmailField(max_length=60)
    password = forms.PasswordInput()
    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]
