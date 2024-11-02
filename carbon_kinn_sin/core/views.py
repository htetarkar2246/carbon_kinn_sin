from rest_framework import viewsets, permissions, status
from .models import StickerCollection, Reward
from .serializers import StickerCollectionSerializer, RewardSerializer
from rest_framework.response import Response
from django.db.models import Count
class StickerCollectionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StickerCollectionSerializer
    queryset = StickerCollection.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        sticker = serializer.validated_data['sticker']
        
        if StickerCollection.objects.filter(user=user, sticker=sticker).exists():
            return Response(
                {"detail": "This sticker has already been collected."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(user=user)

class LeaderboardViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        leaderboard = (
            StickerCollection.objects
            .values('user__id', 'user__name')
            .annotate(sticker_count=Count('sticker'))
            .order_by('-sticker_count')
        )
        
        leaderboard_with_rewards = []
        for entry in leaderboard:
            sticker_count = entry['sticker_count']

            rewards = Reward.objects.filter(threshold__lte=sticker_count).values('name', 'description')
            entry['rewards'] = list(rewards)  # 
            leaderboard_with_rewards.append(entry)

        return Response({'leaderboard': leaderboard_with_rewards})

class RewardViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
