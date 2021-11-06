from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChageForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
        add_form = CustomUserCreationForm
        form = CustomUserChageForm
        model = CustomUser
        list_display = ['email', 'username', 'age', 'is_staff', ]

admin.site.register(CustomUser, CustomUserAdmin)