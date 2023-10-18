from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    list_display = ('email', 'name', 'is_staff', 'have_venues')

    # list_display = ('email', 'document', 'phone', 'birth_date', 'address', 'postal_code', 'is_admin', 'have_venues')
    list_filter = ('is_admin', 'have_venues')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'phone', 'birth_date')}),
        ('Permissions', {'fields': ('is_admin', 'have_venues')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'phone', 'birth_date', 'is_admin', 'have_venues'),
        }),
    )


   

admin.site.register(CustomUser, CustomUserAdmin)
