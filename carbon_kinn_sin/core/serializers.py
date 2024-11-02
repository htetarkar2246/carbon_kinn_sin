from rest_framework import serializers
from .models import StickerCollection, Reward

class StickerCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StickerCollection
        fields = '__all__'

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'
