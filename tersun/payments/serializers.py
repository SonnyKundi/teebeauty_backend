"""Payments serializers file."""

from tersun.payments import models
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

class ProviderPaymentSerializer(serializers.ModelSerializer):
    """Serializer for provider payments."""

    provider_name = ReadOnlyField(source="provider.full_name")

    class Meta:
        """Meta class."""

        model = models.ProviderPayment
        fields = "__all__"
