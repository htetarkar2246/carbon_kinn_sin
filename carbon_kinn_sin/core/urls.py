from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StickerCollectionViewSet, LeaderboardViewSet, RewardViewSet

router = DefaultRouter()
router.register(r'sticker-collections', StickerCollectionViewSet)
router.register(r'rewards', RewardViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('leaderboard/', LeaderboardViewSet.as_view({'get': 'list'}), name='leaderboard'),
]
