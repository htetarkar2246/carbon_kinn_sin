from rest_framework import serializers
from .models import StickerType, Sticker

class StickerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StickerType
        fields = '__all__'

class StickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sticker
        fields = '__all__'