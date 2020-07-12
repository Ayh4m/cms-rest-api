from rest_framework import serializers

from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,                  # Available for create or update only
                'style': {'input_type': 'password'}  # For the browsable API only
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""

        # We override this function to allow it to use the 'create_user' function of the objects manager
        # instead of the default 'create' function of the objects manager which will not hash the password

        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )

        return user
