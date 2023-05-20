"""Serializer file for appointments."""

from tersun.appointments import models
from rest_framework import serializers


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer class for booking."""

    class Meta:
        """Meta class."""

        model = models.Booking
        fields = "__all__"


class BookingServiceSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer class for booking services."""

    class Meta:
        """Meta class."""

        model = models.BookingService
        fields = "__all__"


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer class for appointments."""

    class Meta:
        """Meta class."""

        model = models.Appointment
        fields = "__all__"


class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer class for feedback."""

    class Meta:
        """Meta class."""

        model = models.Feedback
        fields = "__all__"