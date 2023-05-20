"""Views file for appointments."""

from rest_framework import viewsets
from tersun.appointments.models import (Booking, BookingService, Appointment, Feedback)
from tersun.appointments import serializers


class BookingViewSet(viewsets.ModelViewSet):
    """Bookings ViewSet."""

    queryset = Booking.objects.all().order_by('-updated_by')
    serializer_class = serializers.BookingSerializer


class BookingServiceViewSet(viewsets.ModelViewSet):
    """Booking Service ViewSet."""

    queryset = BookingService.objects.all().order_by('-updated_by')
    serializer_class = serializers.BookingServiceSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    """Appointments ViewSet"""

    queryset = Appointment.objects.all().order_by('-updated_by')
    serializer_class = serializers.AppointmentSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    """Feedback ViewSet"""

    queryset = Feedback.objects.all().order_by('-updated_by')
    serializer_class = serializers.FeedbackSerializer
