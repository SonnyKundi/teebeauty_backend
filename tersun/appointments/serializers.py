"""Serializer file for appointments."""

from tersun.appointments import models
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField, SerializerMethodField

class BookingSerializer(serializers.ModelSerializer):
    """Serializer class for booking."""

    service_name = ReadOnlyField(source='service.service_name')
    provider_name = ReadOnlyField(source='service.provider.full_name')

    class Meta:
        """Meta class."""

        model = models.Booking
        fields = "__all__"


class BookingServiceSerializer(serializers.ModelSerializer):
    """Serializer class for booking services."""

    class Meta:
        """Meta class."""

        model = models.BookingService
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    """Serializer class for appointments."""

    class Meta:
        """Meta class."""

        model = models.Appointment
        fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):
    """Serializer class for feedback."""

    class Meta:
        """Meta class."""

        model = models.Feedback
        fields = "__all__"
