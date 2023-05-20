"""Url file for appointments"""

from rest_framework import routers
from tersun.appointments import views

router = routers.DefaultRouter()
router.register(r'bookings', views.BookingViewSet)
router.register(r'booking_services', views.BookingServiceViewSet)
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'feedback', views.FeedbackViewSet)

urlpatterns = router.urls