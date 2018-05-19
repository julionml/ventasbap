from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, CompleteUser

class CustomUserAdmin(UserAdmin):
    model = CompleteUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(CompleteUser, CustomUserAdmin)
