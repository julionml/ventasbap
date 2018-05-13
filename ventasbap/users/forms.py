from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser 
        fields = [
        		'username',
        		'first_name',
        		'last_name',
        		'email',
        	]
        labels = {
        		'username': 'nombre de usuario',
        		'first_name':'Nombre',
        		'last_name': 'Apellidos',
        		'email': 'Correo',
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields