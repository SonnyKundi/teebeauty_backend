"""Views file for providers."""
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from tersun.providers.models import (Provider, ProviderContact)
from tersun.providers import serializers, filters


class ProviderViewSet(viewsets.ModelViewSet):
    """Provider class view set."""

    queryset = Provider.objects.all().order_by('-updated_by')
    serializer_class = serializers.ProviderSerializer
    filterset_class = filters.ProviderFilter
    search_fields = (
        'username', 'first_name', 'last_name', 'other_names', 'email', 'phone_number')

    @action(methods=['post'], detail=False)
    def activate(self, request, *args, **kwargs):
        """Activate api endpoint."""
        user = request.user
        provider = self.get_object()
        provider.activate(user)

        return Response(data={"status": "OK"}, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def terminate(self, request, *args, **kwargs):
        """Terminate api endpoint."""
        user = request.user
        provider = self.get_object()
        provider.terminate(user)

        return Response(data={"status": "OK"}, status=status.HTTP_200_OK)

class ProviderContactViewSet(viewsets.ModelViewSet):
    """Provider class view set."""

    queryset = ProviderContact.objects.all().order_by('-updated_by')
    serializer_class = serializers.ProviderContactSerializer
