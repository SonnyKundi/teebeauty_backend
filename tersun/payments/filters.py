"""Payments filters file."""

import django_filters

from tersun.payments import models
from tersun.common.filters import SearchComboboxBaseFilter


class ProviderPaymentFilter(SearchComboboxBaseFilter):
    """Provider payment filter."""

    class Meta:
        """Meta class for provider payment."""
        model = models.ProviderPayment
        fields = "__all__"
