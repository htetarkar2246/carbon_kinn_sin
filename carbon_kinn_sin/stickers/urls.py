from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StickerTypeViewSet, StickerViewSet

router = DefaultRouter()
router.register(r'sticker-types', StickerTypeViewSet)
router.register(r'stickers', StickerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]