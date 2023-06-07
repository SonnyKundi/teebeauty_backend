"""User serializers file."""

from rest_framework.fields import ReadOnlyField
from rest_framework import serializers

from tersun.users import models

class UserSerializer(serializers.ModelSerializer):
    """Serialize a user, their roles and their permissions."""

    full_name = ReadOnlyField(source='get_full_name', read_only=True)

    def create(self, validated_data):
        user = self.Meta.model.objects.create_user(**validated_data)
        return user

    class Meta:
        """Exclude sensitive fields (e.g password) from being serialized for a user."""

        model = models.User
        fields = (
            'id', 'first_name', 'last_name', 'other_names', 'full_name',
            'username', 'user_type', 'phone_number', 'email', 'date_of_birth',
            'join_date', 'is_staff', 'is_admin', 'is_active', 'password', 'updated_on',)

        extra_kwargs = {
            'password': {'write_only': True}
        }


class MeSerializer(UserSerializer):
    """A special serializer used to serialize the details of the logged in user."""

    class Meta(UserSerializer.Meta):
        """Link the MeSerializer to it's parent's Meta."""

        fields = UserSerializer.Meta.fields
