from django.contrib import admin
from .models import StickerType, Sticker

class StickerTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

class StickerAdmin(admin.ModelAdmin):
    list_display = ('code', 'sticker_type', 'lat', 'lng')
    
admin.site.register(StickerType, StickerTypeAdmin)
admin.site.register(Sticker, StickerAdmin)