"""Views file for providers."""
from rest_framework import viewsets
from tersun.providers.models import (Provider)
from tersun.providers import serializers


class ProviderViewSet(viewsets.ModelViewSet):
    """Provider class view set."""

    queryset = Provider.objects.all().order_by('-updated_by')
    serializer_class = serializers.ProviderSerializer