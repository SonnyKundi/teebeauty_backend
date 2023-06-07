"""Provider's models file."""

import decimal
from django.contrib.auth import get_user_model
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import MinValueValidator
from tersun.common.models import BioData, AbstractBase
from django.db import models
from django.db.models import Q
from tersun.common.utils import get_directory

STATUS_CHOICES = (
    ("ACTIVE", "ACTIVE"),
    ("LAPSED", "LAPSED"),
    ("TERMINATED", "TERMINATED"),
)

ACTIVE = "ACTIVE"
TERMINATED = "TERMINATED"
LAPSED = "LAPSED"

# TODO Add user id field to identify the provider by their user profile
# Validate a user with the given user id has only one provider instance
# Make the email field unique
# Connect a new user or saved user instance to the provider by email

class Provider(BioData):
    """Provider models."""

    username = models.CharField(max_length=300, null=False, blank=False)
    provider_number = models.CharField(max_length=300, null=True, blank=True)
    profile_image = models.FileField(upload_to=get_directory)
    status = models.CharField(
        max_length=300, null=False, blank=False, choices=STATUS_CHOICES, default=ACTIVE)
    user_id = models.UUIDField(null=True, blank=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def amount_due(self):
        """Get the amount due."""
        provider_subscriptions = ProviderSubscription.objects.filter(provider=self)
        if not provider_subscriptions.exists():
            return 0

        latest_subscription = provider_subscriptions.latest('subscription_date')
        return latest_subscription.amount_due

    def activate(self, user=None):
        """Activate a provider."""
        self.status = ACTIVE
        self.updated_by = user.id if user else self.updated_by
        self.is_active = True
        self.save()

    def terminate(self, user=None):
        """Terminate a provider."""
        self.status = TERMINATED
        self.is_active = False
        self.updated_by = user.id if user else self.updated_by
        self.save()

    def lapse(self):
        self.status = LAPSED
        self.is_active = False
        self.save()

    def validate_user_has_one_provider_instance(self):
        """Validate that the user has only one provider instance."""
        if self.user_id:
            if self.__class__.objects.filter(user_id=self.user_id).exclude(id=self.id).exists():
                msg = "a different provider is already assigned to this user"
                raise ValidationError({'user': msg})

    def get_user_id(self):
        """Get user to whom this provider belongs."""
        user = get_user_model().objects.filter(Q(email=self.email) | Q(username=self.username))
        if user.exists():
            user = user.first()
            self.user_id = user.id

    def clean(self) -> None:
        self.validate_user_has_one_provider_instance()
        return super().clean()

    def save(self, *args, **kwargs):
        self.get_user_id()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        """String representation."""
        return self.first_name +" " + " " + self.last_name


class ProviderContact(AbstractBase):
    """Provider contacts model."""

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    email = models.EmailField(max_length=300, null=True, blank=True, verbose_name="business_email")
    phone_number = models.CharField(max_length=300, null=True, blank=True, verbose_name="business_phone_number")
    whatsapp_number = models.CharField(max_length=300, null=True, blank=True, verbose_name="business_whatsapp_number")
    twitter_link = models.URLField(null=True, blank=True, max_length=500)
    instagram_link = models.URLField(null=True, blank=True, max_length=500)
    facebook_link = models.URLField(null=True, blank=True, max_length=500)
    tiktok_link = models.URLField(null=True, blank=True, max_length=500)
    youtube_link = models.URLField(null=True, blank=True, max_length=500)
    website_link = models.URLField(null=True, blank=True, max_length=500, verbose_name="business_profile_website")


class ProviderSubscription(AbstractBase):
    """Provider Sessions model"""
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    speculated_end_date = models.DateTimeField()
    total_charge = models.DecimalField(
        max_digits=30, decimal_places=2, null=False, blank=False,
        validators=[MinValueValidator(0.00)], default=0)
    discount_amount = models.DecimalField(
        max_digits=30, decimal_places=2, null=True, blank=True,
        validators=[MinValueValidator(0.00)], default=0)
    amount_paid = models.DecimalField(
        max_digits=30, decimal_places=2, null=False, blank=False,
        validators=[MinValueValidator(0.00)], default=0)
    subscription_date = models.DateTimeField(default=timezone.now)
    payment_id = models.UUIDField(null=False, blank=False)

    @property
    def amount_due(self):
        """Get the amount due."""
        return self.total_charge - self.discount_amount - self.amount_paid

    def get_speculated_end_date(self):
        self.speculated_end_date = self.start_date + timedelta(30)

    def save(self, *args, **kwargs):
        self.total_charge = decimal.Decimal(1250)
        self.get_speculated_end_date()
        return super().save(*args, **kwargs)
