from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'ph_num', 'is_staff', 'is_active')
    search_fields = ('email', 'name', 'ph_num')
    list_filter = ('is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'ph_num')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'ph_num', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )

    ordering = ('email',)
    
    def has_add_permission(self, request):
        return False


admin.site.register(User, UserAdmin)
