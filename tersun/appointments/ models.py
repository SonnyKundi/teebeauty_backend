"""Appointments models file."""

from tersun.common.models import AbstractBase
from tersun.provider_services.models import Service
from django.db import models
from django.core.validators import MinValueValidator

APPOINTMENT_STATUS_CHOICES = (
    ("IN SERVICE", "IN SERVICE"),
    ("FULFILLED", "FULFILLED"),
    ("DUE", "DUE"),
    ("CANCELED", "CANCELED"),
)

REVIEWER_CHOICES = (
    ("PROVIDER", "PROVIDER"),
    ("CLIENT", "CLIENT"),
)

class Booking(AbstractBase):
    """Bookings model."""

    services = models.ManyToManyField(through="BookingService")
    time = models.DateTimeField(null=False, blank=False)
    location = models.CharField(max_length=300, null=False, blank=False)
    house_call = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=300, null=False, blank=False)
    pricing = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0.00)], default=0)
    email = models.EmailField(max_length=300, null=True, blank=True)
    booking_charge = models.DecimalField(max_digits=30, decimal_places=2,null=True, blank=True, validators=[MinValueValidator(0.00)], default=0)
    paid = models.BooleanField(default=False)


class BookingService(AbstractBase):
    """Bookings Services models."""

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    

class Appointment(AbstractBase):
    """Appointments model."""

    booking = models.ForeignKey(Booking, on_delete=models.PROTECT)
    deposit = models.DecimalField(max_digits=30, decimal_places=2,null=False, blank=False, validators=[MinValueValidator(0.00)], default=0)
    appointment_fee = models.DecimalField(max_digits=30, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(0.00)], default=0)
    appointment_status = models.CharField(max_length=300, choices=APPOINTMENT_STATUS_CHOICES)


class Feedback(AbstractBase):
    """Feedback model."""

    appointment = models.ForeignKey(Appointment, on_delete=models.PROTECT)
    reviewer =  models.CharField(max_length=300, choices=REVIEWER_CHOICES)
    response_score = models.IntegerField(null=True, blank=True, default=0)
    punctuality_score = models.IntegerField(null=True, blank=True, default=0)
    quality_of_work_score = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField()
    
