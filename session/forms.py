from django import forms
from User.models import User

class login(forms.ModelForm):
    id_card = forms.CharField(max_length=15)
    password = forms.PasswordInput()
    class Meta:
        model = User
        fields = [
            'id_card',
            'password',
        ]
