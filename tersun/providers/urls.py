"""Url file for provider services."""

from rest_framework import routers
from tersun.providers import views

router = routers.DefaultRouter()
router.register(r'providers', views.ProviderViewSet)
router.register(r'provider_contacts', views.ProviderContactViewSet)

urlpatterns = router.urls
