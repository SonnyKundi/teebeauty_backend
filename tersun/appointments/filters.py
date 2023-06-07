"""Appointments filters file."""

import django_filters
from django.db import models

from tersun.appointments.models import Booking
from tersun.common.filters import SearchComboboxBaseFilter


class BookingFilter(SearchComboboxBaseFilter):
    """Booking filter class."""

    provider_user_id = django_filters.CharFilter(method='filter_by_provider_user_id')

    def filter_by_provider_user_id(self, queryset, name, value):
        if value:
            return queryset.filter(service__provider__user_id=value)
        return queryset

    class Meta:
        """Meta class for the bookings filter."""

        model = Booking
        fields = "__all__"
