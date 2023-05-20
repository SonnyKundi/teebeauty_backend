"""Url file for provider services."""

from rest_framework import routers
from tersun.providers import views

router = routers.DefaultRouter()
router.register(r'providers', views.ProviderViewSet)

urlpatterns = router.urls