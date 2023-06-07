"""Payments urls file."""

from rest_framework import routers

from tersun.payments import views

router = routers.DefaultRouter()
router.register('provider_payments', views.ProviderPaymentViewSet)

urlpatterns = router.urls
