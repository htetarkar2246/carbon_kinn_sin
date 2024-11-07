from django.contrib import admin
from .models import StickerType, Sticker

class StickerTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('name',)

class StickerAdmin(admin.ModelAdmin):
    list_display = ('id', 'sticker_type', 'lat', 'lng','image')
    search_fields = ('sticker_type__name',)
    list_filter = ('sticker_type',)

admin.site.register(StickerType, StickerTypeAdmin)
admin.site.register(Sticker, StickerAdmin)

