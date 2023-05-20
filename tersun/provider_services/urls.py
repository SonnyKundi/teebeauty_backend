"""Url file for provider services."""

from rest_framework import routers
from tersun.provider_services import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'sub categories', views.SubCategoryViewSet)
router.register(r'towns', views.TownViewSet)
router.register(r'services', views.ServiceViewSet)
router.register(r'service_sub_categories', views.ServiceSubCategoryViewSet)
router.register(r'service_towns', views.ServiceTownViewSet)
router.register(r'service_images', views.ServiceImageViewSet)
router.register(r'service_videos', views.ServiceVideoViewSet)

urlpatterns = router.urls