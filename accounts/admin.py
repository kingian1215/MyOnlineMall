from django.contrib import admin
from.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ('username', 'is_student', 'is_teacher', 'is_approved','is_staff')
    list_filter = ('is_student', 'is_teacher', 'is_approved')
    fieldsets = (
        (None, {'fields': ('username','password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_approved', 'is_student', 'is_teacher')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_student', 'is_teacher', 'is_approved')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)