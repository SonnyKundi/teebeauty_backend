"""Payments views file."""

from rest_framework import viewsets

from tersun.payments.models import ProviderPayment
from tersun.payments import serializers, filters

class ProviderPaymentViewSet(viewsets.ModelViewSet):
    """Provider payment viewset."""

    queryset = ProviderPayment.objects.all().order_by("-updated_on")
    serializer_class = serializers.ProviderPaymentSerializer
    filterset_class = filters.ProviderPaymentFilter
    search_fields = (
        'provider__first_name', 'provider__last_name', 'provider__other_names',
        'provider__email', 'provider__username', 'provider__provider_number',
        'amount_paid', 'receipt_number', 'payment_method', 'payment_code')
