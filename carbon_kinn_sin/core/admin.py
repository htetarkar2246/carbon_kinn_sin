from django.contrib import admin
from .models import StickerCollection, Reward

class StickerCollectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sticker', 'collected_at')
    list_filter = ('user', 'sticker', 'collected_at')  
    search_fields = ('user__name', 'sticker__code')
    ordering = ('-collected_at',)  
    list_per_page = 20  
    
    def has_add_permission(self, request):
        return False

class RewardAdmin(admin.ModelAdmin):
    list_display = ('name', 'threshold', 'tier') 
    list_filter = ('tier',)  
    search_fields = ('name',)
    ordering = ('threshold',) 
    list_per_page = 10  

admin.site.register(StickerCollection, StickerCollectionAdmin)
admin.site.register(Reward, RewardAdmin)
