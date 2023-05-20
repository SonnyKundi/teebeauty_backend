"""Serializers file for provider services."""

from tersun.providers import models
from rest_framework import serializers


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for providers."""

    class Meta:
        """Meta class."""

        model = models.Provider
        fields = "__all__"
