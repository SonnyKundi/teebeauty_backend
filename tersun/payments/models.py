"""Payments models file."""

from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

from tersun.common.models import AbstractBase
from tersun.providers.models import Provider

PAYMENT_METHOD_CHOICES = (
    ('PDQ', 'PDQ'),
    ('CASH', 'CASH'),
    ('CARD', 'CARD'),
    ('WALLET', 'WALLET'),
    ('MPESA TILL', 'MPESA TILL'),
    ('MPESA PAYBILL', 'MPESA PAYBILL'),
    ('BANK TRANSFER', 'BANK TRANSFER'),
    ('BANK CHEQUE', 'BANK CHEQUE'),
)


class ProviderPayment(AbstractBase):
    """Provider payments model."""

    provider = models.ForeignKey(Provider, on_delete=models.PROTECT)
    amount_paid = models.DecimalField(
        max_digits=30, decimal_places=2,null=False, blank=False,
        validators=[MinValueValidator(0.00)], default=0)
    receipt_number = models.CharField(max_length=300, null=False, blank=False)
    payment_method = models.CharField(
        max_length=300, null=False, blank=False, choices=PAYMENT_METHOD_CHOICES)
    payment_code = models.CharField(max_length=300, null=True, blank=True)
    payment_date = models.DateTimeField(db_index=True, default=timezone.now)

    def save_provider_subscription(self):
        """Save the provider subscription."""
        from tersun.providers.models import ProviderSubscription

        provider_subscriptions = ProviderSubscription.objects.filter(provider=self.provider).exclude(payment_id=self.id)
        balance_amount = self.amount_paid

        if provider_subscriptions.exists():
            latest_provider_subscription = provider_subscriptions.latest("subscription_date")
            if latest_provider_subscription.amount_due > 0:
                amount_payable = latest_provider_subscription.amount_due
                balance_amount -= amount_payable
                if latest_provider_subscription.amount_due > balance_amount:
                    amount_payable = balance_amount
                    balance_amount = 0

                latest_provider_subscription.amount_paid += amount_payable
                latest_provider_subscription.save()

        if balance_amount > 0:
            # Create a new subscription or update the old one.
            subscription = ProviderSubscription.objects.filter(payment_id=self.id)
            if not subscription.exists():
                subscription_data = {
                    "created_by": self.created_by,
                    "updated_by": self.updated_by,
                    "payment_id": self.id,
                    "provider": self.provider,
                    "start_date": timezone.now(),
                    "subscription_date": timezone.now(),
                    "amount_paid": balance_amount,
                }
                ProviderSubscription.objects.create(**subscription_data)
                return

            subscription = subscription.first()
            subscription.amount_paid = balance_amount
            subscription.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # self.save_provider_subscription()
