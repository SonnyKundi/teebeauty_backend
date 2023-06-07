"""Providers filters file."""

from django.db import models
import django_filters

from tersun.common.filters import SearchComboboxBaseFilter
from tersun.providers import models as provider_models


class ProviderFilter(SearchComboboxBaseFilter):
    """Provider filter class."""

    class Meta:
        """Meta class for the providers filter."""

        model = provider_models.Provider
        fields = "__all__"
        filter_overrides = {
             models.FileField: {
                 'filter_class': django_filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
        }