"""Serializers file for provider services."""

from tersun.provider_services import models
from tersun.providers.models import ProviderContact
from tersun.providers.serializers import ProviderContactSerializer

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, CharField, ReadOnlyField, FileField


class CategorySerializer(serializers.ModelSerializer):
    """Serializer class for categories."""

    class Meta:
        """Meta class."""

        model = models.Category
        fields = "__all__"
    

class SubCategorySerializer(serializers.ModelSerializer):
    """Serializer class for subcategories."""

    class Meta:
        """Meta class."""

        model = models.SubCategory
        fields = "__all__"


class TownSerializer(serializers.ModelSerializer):
    """Serializer class for towns."""

    class Meta:
        """Meta class."""

        model = models.Town
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    """Serializer class for service"""

    provider_name=ReadOnlyField(source='provider.full_name')
    profile_image=FileField(source='provider.profile_image')
    username=ReadOnlyField(source='provider.username')
    categories=ReadOnlyField()
    average_ratings = SerializerMethodField()
    locations = ReadOnlyField()
    images = SerializerMethodField()
    sub_categories = SerializerMethodField()
    contacts = SerializerMethodField()

    def get_average_ratings(self, instance):
        """Get average rating."""
        ratings = models.Rating.objects.filter(service=instance).values_list("rating", flat=True)
        count = models.Rating.objects.filter(service=instance).count()
        if count <= 0:
            return {"rating": 0, "count":0}
        return {"rating": sum(ratings)/count, "count": count}

    def get_images(self, instance):
        """Get images."""
        images = models.ServiceImage.objects.filter(service=instance)
        
        return ServiceImageSerializer(images, many=True).data

    def get_sub_categories(self, instance):
        """Get sub categories function."""
        return SubCategorySerializer(instance.sub_categories, many=True).data

    def get_contacts(self, instance):
        """Get contacts function."""
        provider_contacts = ProviderContact.objects.filter(provider=instance.provider)
        if provider_contacts.exists():
            provider_contact = provider_contacts.latest('updated_on')
            return ProviderContactSerializer(provider_contact, many=False).data

        return {}

    class Meta:
        """Meta class"""

        model = models.Service
        fields = "__all__"


class ServiceSubCategorySerializer(serializers.ModelSerializer):
    """Serializer class for service sub category."""

    class Meta:
        """Meta class"""

        model = models.ServiceSubCategory
        fields = "__all__"


class ServiceTownSerializer(serializers.ModelSerializer):
    """Serializer class for service town."""

    class Meta:
        """Meta class"""

        model = models.ServiceTown
        fields = "__all__"


class ServiceImageSerializer(serializers.ModelSerializer):
    """Serializer class for service image."""

    class Meta:
        """Meta class."""

        model = models.ServiceImage
        fields = "__all__"


class ServiceVideoSerializer(serializers.ModelSerializer):
    """Serializer class for service video."""

    class Meta:
        """Meta class."""

        model = models.ServiceVideo
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    """Serializer class for ratings."""

    class Meta:
        """Meta class."""

        model = models.Rating
        fields = "__all__"
