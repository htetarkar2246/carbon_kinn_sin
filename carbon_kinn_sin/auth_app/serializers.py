from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'ph_num', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Password is write-only
            'email': {'required': True}  # Make email a required field
        }

    def create(self, validated_data):
        """Create and return a new user instance, using hashed password."""
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user
