from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'user') 
    list_filter = ('created_at', 'user')  
    search_fields = ('name', 'email', 'message')  
    readonly_fields = ('name', 'email', 'message', 'created_at', 'user') 

    def has_add_permission(self, request):
        return False

admin.site.register(ContactMessage, ContactMessageAdmin)