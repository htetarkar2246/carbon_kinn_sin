from django.contrib.auth import get_user_model
from django.db import models
from stickers.models import Sticker

User = get_user_model()
class StickerCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sticker = models.ForeignKey(Sticker, on_delete=models.CASCADE)
    collected_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'sticker')

    def __str__(self):
        return f"{self.user.email} collected {self.sticker.code}"

class Reward(models.Model):
    TIER_CHOICES = [
        (1, 'Tier 1: Completion of 1 Theme'),
        (2, 'Tier 2: Completion of 3 Themes'),
        (3, 'Tier 3: Completion of All Themes'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    threshold = models.PositiveIntegerField()  
    tier = models.PositiveSmallIntegerField(choices=TIER_CHOICES, unique=True)

    def __str__(self):
        return self.name
