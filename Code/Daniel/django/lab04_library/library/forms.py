from django.contrib.auth.models import User
from django.forms import ModelForm

class User_Form(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        help_texts = {
            'username': None,
        }


class Login_Form(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        help_texts = {
            'username': None,
        }