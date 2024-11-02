from rest_framework import viewsets
from .models import StickerType, Sticker
from .serializers import StickerTypeSerializer, StickerSerializer
from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users to edit objects.
    All other users can view objects but not modify them.
    """

    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True
        # If the request method is safe (GET, HEAD, OPTIONS), allow access
        return request.method in permissions.SAFE_METHODS
      
class StickerTypeViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing Sticker Types.
    Only admin users can create, update, or delete sticker types.
    """
    permission_classes = [permissions.IsAdminUser]
    queryset = StickerType.objects.all()
    serializer_class = StickerTypeSerializer


class StickerViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing Stickers.
    Admin users can create, update, or delete stickers,
    while authenticated users can read the sticker data.
    """
    permission_classes = [IsAdminUserOrReadOnly]  
    queryset = Sticker.objects.all()
    serializer_class = StickerSerializer