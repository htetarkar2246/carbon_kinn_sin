from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    """API view to create a new user."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """Handle user creation."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Validate input data
        user = serializer.save()  # Save the new user
        return Response({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'ph_num': user.ph_num
        }, status=status.HTTP_201_CREATED)
