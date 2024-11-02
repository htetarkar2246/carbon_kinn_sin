from rest_framework import viewsets, permissions
from .models import StickerCollection, Reward
from .serializers import StickerCollectionSerializer, RewardSerializer
from rest_framework.response import Response
from django.db.models import Count

class StickerCollectionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StickerCollectionSerializer
    queryset = StickerCollection.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LeaderboardViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        leaderboard = (
            StickerCollection.objects
            .values('user__name')
            .annotate(sticker_count=Count('sticker'))
            .order_by('-sticker_count')
        )
        
        return Response({'leaderboard': leaderboard})

class RewardViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
