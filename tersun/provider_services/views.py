"""Views file for provider services"""

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from tersun.providers.models import Provider
from tersun.provider_services.models import (
    Category, SubCategory, Town, Service, ServiceSubCategory,
    ServiceTown, ServiceImage, ServiceVideo, Rating)
from tersun.provider_services import serializers, filters

class CategoryViewSet(viewsets.ModelViewSet):
    """Category View Set."""

    queryset = Category.objects.all().order_by('-updated_on')
    serializer_class = serializers.CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    """Sub Category View Set."""

    queryset = SubCategory.objects.all().order_by('-updated_on')
    serializer_class = serializers.SubCategorySerializer


class TownViewSet(viewsets.ModelViewSet):
    """Town View Set."""

    queryset = Town.objects.all().order_by('-updated_on')
    serializer_class = serializers.TownSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """Service View Set."""

    queryset = Service.objects.all().order_by('-updated_on')
    serializer_class = serializers.ServiceSerializer
    filterset_class = filters.ServiceFilter
    search_fields = (
        'service_name', 'description')

    @action(methods=['post'], detail=False)
    def new_service(self, request, *args, **kwargs):
        """Custom new service endpoint to handle the creation of a new service from the backend."""
        my_data = dict(request.data)
        provider_data = {
            "created_by": "85ca1206-4461-4924-a78a-8854b5c5e450",
            "updated_by": "85ca1206-4461-4924-a78a-8854b5c5e450",
            "username": my_data.get("username")[0],
            "first_name": my_data.get("first_name")[0],
            "last_name": my_data.get("last_name")[0],
            "email": my_data.get("email")[0],
            "phone_number": my_data.get("phone_number")[0],
            "profile_image": my_data.get("profile_image")[0],
        }
        provider = Provider.objects.create(**provider_data)
        service_data = {
                "created_by": "85ca1206-4461-4924-a78a-8854b5c5e450",
                "updated_by": "85ca1206-4461-4924-a78a-8854b5c5e450",
                "provider": provider,
                "service_name": provider.full_name,
                "house_calls": True if my_data.get("house_calls")[0]=="true" else False,
                "minimum_charge": my_data.get("minimum_charge")[0],
                "description": my_data.get("description")[0],
                "billboard_image": my_data.get("billboard_image")[0],
        }
        service = Service.objects.create(**service_data)
        town_id = my_data.get("towns")[0]
        town = Town.objects.filter(id=town_id).first()
        if town:
            ServiceTown.objects.create(
                    service=service, town=town,
                    created_by="85ca1206-4461-4924-a78a-8854b5c5e450",
                    updated_by="85ca1206-4461-4924-a78a-8854b5c5e450",
                    )
        images = my_data.get("images")
        if len(images) >= 1:
            for image in images:
                ServiceImage.objects.create(
                        service=service, image=image,
                        created_by="85ca1206-4461-4924-a78a-8854b5c5e450",
                        updated_by="85ca1206-4461-4924-a78a-8854b5c5e450",
                    )

        category_ids = my_data.get("categories")[0]
        category_ids = category_ids.split(",")
        if len(category_ids) >= 1:
            categories = Category.objects.filter(id__in=category_ids)
            sub_categories = SubCategory.objects.filter(category__in=categories)
            for sub_category in sub_categories:
                ServiceSubCategory.objects.create(
                    service=service, sub_category=sub_category,
                    created_by="85ca1206-4461-4924-a78a-8854b5c5e450",
                    updated_by="85ca1206-4461-4924-a78a-8854b5c5e450",
                )

        data = data = self.get_serializer(service).data
        return Response(data=data, status=status.HTTP_201_CREATED)

class ServiceSubCategoryViewSet(viewsets.ModelViewSet):
    """Service Sub Category View Set."""

    queryset = ServiceSubCategory.objects.all().order_by('-updated_on')
    serializer_class = serializers.ServiceSubCategorySerializer


class ServiceTownViewSet(viewsets.ModelViewSet):
    """Service Town View Set."""

    queryset = ServiceTown.objects.all().order_by('-updated_on')
    serializer_class = serializers.ServiceTownSerializer


class ServiceImageViewSet(viewsets.ModelViewSet):
    """Service Image View Set."""

    queryset = ServiceImage.objects.all().order_by('-updated_on')
    serializer_class = serializers.ServiceImageSerializer


class ServiceVideoViewSet(viewsets.ModelViewSet):
    """Service Video View Set."""

    queryset = ServiceVideo.objects.all().order_by('-updated_on')
    serializer_class = serializers.ServiceVideoSerializer


class RatingViewSet(viewsets.ModelViewSet):
    """Service Video View Set."""

    queryset = Rating.objects.all().order_by('-updated_on')
    serializer_class = serializers.RatingSerializer
