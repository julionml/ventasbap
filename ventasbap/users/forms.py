from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from .models import CompleteUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CompleteUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'City',
            'Bdate',
            'sex',
            'Id',
            'cellphone',

        ]
        labels = dict(username='Nombre de usuario', first_name='Nombre', last_name='Apellidos', email='Correo',
                      City='Ciudad', Bdate='Fecha de nacimiento', sex='género', Id='Cedula de Identidad',
                      cellphone='telefono')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CompleteUser
        fields = UserChangeForm.Meta.fields
