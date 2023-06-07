from django.db import models
from tersun.common.models import AbstractBase
from tersun.providers.models import Provider
from django.core.validators import MinValueValidator
from tersun.common.utils import get_directory



class Category(AbstractBase):
    """Categories model."""

    category_name = models.CharField(max_length=300, null=False, blank=False)
    category_code = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self) -> str:
        return self.category_name


class SubCategory(AbstractBase):
    """Sub Categories model."""

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=300, null=False, blank=False)
    sub_category_code = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self) -> str:
        return self.category.category_name + " -> " + self.sub_category_name


# T0DO Create Location Model from where service providers can specify specific locations.
# For example Nairobi -> Westlands, Parklands, Kilimani etc.
class Town(AbstractBase):
    """Towns model."""

    county = models.CharField(max_length=300, null=False, blank=False)
    town_name = models.CharField(max_length=300, null=False, blank=False)
    town_code = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self) -> str:
        return "{}, {}".format(self.town_name, self.county)


# TODO Refactor Towns to use Locations instead.
class Service(AbstractBase):
    """Services model."""

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=300, null=True, blank=True)
    sub_categories = models.ManyToManyField(SubCategory, through="ServiceSubCategory")
    house_calls = models.BooleanField(default=False)
    minimum_charge = models.DecimalField(max_digits=30, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(0.00)], default=0)
    towns = models.ManyToManyField(Town, through="ServiceTown")
    description = models.TextField()
    billboard_image = models.FileField(upload_to=get_directory)

    @property
    def categories(self):
        """Get categories."""
        categories = list(set(ServiceSubCategory.objects.filter(service=self).values_list('sub_category__category__category_name', flat=True)))
        return categories

    @property
    def locations(self):
        """Get the towns the service is available."""
        service_towns = ServiceTown.objects.filter(service=self)
        if not service_towns.exists():
            return []

        locations = []
        for service_town in service_towns:
            location = f"{service_town.town.town_name}, {service_town.town.county}"
            locations.append(location)

        return locations

    @property
    def average_rating(self):
        """Get average rating."""
        ratings = Rating.objects.filter(service=self).values_list("rating", flat=True)
        count = Rating.objects.filter(service=self).count()
        if count <= 0:
            return 0
        return sum(ratings)/count

    def __str__(self) -> str:
        return self.service_name


class ServiceSubCategory(AbstractBase):
    """Services Sub Categories through model."""

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)


class ServiceTown(AbstractBase):
    """Service Town through model."""
    
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    town = models.ForeignKey(Town, on_delete=models.PROTECT)


class ServiceImage(AbstractBase):
    """Service Images through model."""

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    image = models.FileField(upload_to=get_directory, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)


class ServiceVideo(AbstractBase):
    """Service Videos through model."""

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    video = models.FileField(upload_to=get_directory, null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)


class Rating(AbstractBase):
    """Rating class."""

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
