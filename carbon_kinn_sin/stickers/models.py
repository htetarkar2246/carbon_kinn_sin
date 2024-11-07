from django.db import models

class StickerType(models.Model):
    name = models.CharField(max_length=100)
   
    def __str__(self):
        return self.name

class Sticker(models.Model):
    code = models.CharField(max_length=20, unique=True)  
    sticker_type = models.ForeignKey(StickerType, related_name='stickers', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='core/media')  
    lat = models.FloatField()  # Latitude for geographical location
    lng = models.FloatField()  # Longitude for geographical location

    def __str__(self):
        return f"{self.code} - {self.sticker_type.name}"