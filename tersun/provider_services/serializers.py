"""Serializers file for provider services."""

from tersun.provider_services import models
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """Serializer class for categories."""

    class Meta:
        """Meta class."""

        model = models.Category
        fields = "__all__"
    

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    """Serializer class for subcategories."""

    class Meta:
        """Meta class."""

        model = models.SubCategory
        fields = "__all__"


class TownSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer class for towns."""

    class Meta:
        """Meta class."""

        model = models.Town
        fields = "__all__"


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer class for service"""

    class Meta:
        """Meta class"""

        model = models.Service
        fields = "__all__"


class ServiceSubCategorySerializer(serializers.HyperlinkedModelSerializer):
    """Serializer class for service sub category."""

    class Meta:
        """Meta class"""

        model = models.ServiceSubCategory
        fields = "__all__"


class ServiceTownSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer class for service town."""

    class Meta:
        """Meta class"""

        model = models.ServiceTown
        fields = "__all__"


class ServiceImageSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer class for service image."""

    class Meta:
        """Meta class."""

        model = models.ServiceImage
        fields = "__all__"


class ServiceVideoSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer class for service video."""

    class Meta:
        """Meta class."""

        model = models.ServiceVideo
        fields = "__all__"