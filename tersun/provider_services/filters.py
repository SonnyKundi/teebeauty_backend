"""Provider services filters file."""
from tersun.provider_services import models as services_models
from tersun.common.filters import SearchComboboxBaseFilter

import django_filters
from django.db import models

class ServiceFilter(SearchComboboxBaseFilter):
    """Service filter."""
    town = django_filters.CharFilter(method='filter_by_town')
    county = django_filters.CharFilter(method='filter_by_county')
    category = django_filters.CharFilter(method='filter_by_category')
    sub_category = django_filters.CharFilter(method='filter_by_sub_category')
    average_rating = django_filters.CharFilter(method='filter_by_average_rating')

    def filter_by_town(self, queryset, name, value):
        if value:
            return queryset.filter(towns__town_name=value)
        return queryset

    def filter_by_county(self, queryset, name, value):
        if value:
            return queryset.filter(towns__county=value)
        return queryset

    def filter_by_category(self, queryset, name, value):
        if value:
            service_ids = list(set(map(str, queryset.filter(sub_categories__category__category_name=value).values_list("id", flat=True))))
            return queryset.filter(id__in=service_ids)
        return queryset

    def filter_by_sub_category(self, queryset, name, value):
        if value:
            return queryset.filter(sub_categories__sub_category_name=value)
        return queryset

    def filter_by_average_rating(self, queryset, name, value):
        if value:
            services_ids=[]
            for service in queryset:
                if service.average_rating < float(value):
                    continue
                services_ids.append(service.id)
            return queryset.filter(id__in=services_ids)
        return queryset

    class Meta:
        model = services_models.Service
        fields = "__all__"
        filter_overrides = {
             models.FileField: {
                 'filter_class': django_filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
        }
