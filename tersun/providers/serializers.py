"""Serializers file for provider services."""

from tersun.providers import models
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField, SerializerMethodField

class ProviderSerializer(serializers.ModelSerializer):
    """Serializer for providers."""

    full_name=ReadOnlyField()
    amount_due = ReadOnlyField()
    whatsapp_number = SerializerMethodField()

    def get_whatsapp_number(self, instance):
        """Get whatsapp number."""
        contact = models.ProviderContact.objects.filter(provider=instance).first()
        if not contact:
            return instance.phone_number

        return contact.whatsapp_number

    class Meta:
        """Meta class."""

        model = models.Provider
        fields = "__all__"


class ProviderContactSerializer(serializers.ModelSerializer):
    """Serializer for providers."""

    class Meta:
        """Meta class."""

        model = models.ProviderContact
        fields = "__all__"
