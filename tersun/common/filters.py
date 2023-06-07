"""Common filters file."""

from django.db.models import Case, IntegerField, Value, When
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter


class SearchComboboxBaseFilter(filters.FilterSet):
    """Ensure that combobox results always include the selected item.

    This should be the case even if the selected record would not ordinarily be on the first
    page of a paginated result set.
    """

    def combobox_filter(self, queryset, field, value):
        """Annotate the queryset to ensure that the selected item is always first on the list."""
        # annotate with a field called 'custom_order' that places the combobox supplied value first
        # this ensures that the selected item shows up at the top, even if there are very many
        # results
        ordering_filters = (
            'custom_order', '-updated_on') if hasattr(
                self.Meta().model, 'created_on') else ('custom_order', '-updated_on')

        return queryset.annotate(
            custom_order=Case(
                When(pk__in=value.split(','), then=Value(0)),
                output_field=IntegerField(),
                default=Value(1))).order_by(*ordering_filters)

    search = SearchFilter()
    combobox = filters.CharFilter(method='combobox_filter')
