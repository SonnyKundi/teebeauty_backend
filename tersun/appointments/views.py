"""Views file for appointments."""

from rest_framework import viewsets
from tersun.appointments.models import (Booking, BookingService, Appointment, Feedback)
from tersun.appointments import serializers, filters


class BookingViewSet(viewsets.ModelViewSet):
    """Bookings ViewSet."""

    queryset = Booking.objects.all().order_by('-updated_by')
    serializer_class = serializers.BookingSerializer
    filterset_class = filters.BookingFilter
    search_fields = (
        'phone_number', 'whatsapp_number', 'email', 'service__service_name',
        'service__provider__first_name', 'service__provider__last_name',
        'service__provider__other_names', 'service__provider__email',
        'service__provider__phone_number')

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
