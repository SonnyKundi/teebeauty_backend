"""Views file for provider services"""
from rest_framework import viewsets
from tersun.provider_services.models import (
    Category, SubCategory, Town, Service, ServiceSubCategory,
    ServiceTown, ServiceImage, ServiceVideo)
from tersun.provider_services import serializers

class CategoryViewSet(viewsets.ModelViewSet):
    """Category View Set."""

    queryset = Category.objects.all().order_by('-updated_by')
    serializer_class = serializers.CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    """Sub Category View Set."""

    queryset = SubCategory.objects.all().order_by('-updated_by')
    serializer_class = serializers.SubCategorySerializer


class TownViewSet(viewsets.ModelViewSet):
    """Town View Set."""

    queryset = Town.objects.all().order_by('-updated_by')
    serializer_class = serializers.TownSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """Service View Set."""

    queryset = Service.objects.all().order_by('-updated_by')
    serializer_class = serializers.ServiceSerializer


class ServiceSubCategoryViewSet(viewsets.ModelViewSet):
    """Service Sub Category View Set."""

    queryset = ServiceSubCategory.objects.all().order_by('-updated_by')
    serializer_class = serializers.ServiceSubCategorySerializer


class ServiceTownViewSet(viewsets.ModelViewSet):
    """Service Town View Set."""

    queryset = ServiceTown.objects.all().order_by('-updated_by')
    serializer_class = serializers.ServiceTownSerializer


class ServiceImageViewSet(viewsets.ModelViewSet):
    """Service Image View Set."""

    queryset = ServiceImage.objects.all().order_by('-updated_by')
    serializer_class = serializers.ServiceImageSerializer


class ServiceVideoViewSet(viewsets.ModelViewSet):
    """Service Video View Set."""

    queryset = ServiceVideo.objects.all().order_by('-updated_by')
    serializer_class = serializers.ServiceVideoSerializer




