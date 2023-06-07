"""Common models file for tersun."""
import uuid
from django.db import models
from django.utils import timezone

GENDER_CHOICES = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ('OTHER', 'OTHER'),
)

class AbstractBase(models.Model):
    """Base for all models."""
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True, auto_created=True)
    created_on = models.DateTimeField(
        db_index=True, editable=False, default=timezone.now)
    created_by = models.UUIDField(editable=True)
    updated_on = models.DateTimeField(db_index=True, default=timezone.now)
    updated_by = models.UUIDField()
    is_active = models.BooleanField(default=True)

    def retain_created_on_and_created_by(self):
        """Retain values for created_on and created_by fields on update."""
        try:
            initial = self.__class__.objects.get(pk=self.pk)
            self.created_on = initial.created_on
            self.created_by = initial.created_by
        except self.__class__.DoesNotExist:
            pass

    def save(self, *args, **kwargs):
        """Record today as the update date."""
        self.updated_on = timezone.now()
        self.full_clean(exclude=None)
        self.retain_created_on_and_created_by()
        super(AbstractBase, self).save(*args, **kwargs)

    class Meta:
        """Initialize as meta class
        and
        order by descending dates starting with updated by.
        """

        abstract = True
        ordering = ('-updated_on', '-created_on')


class BioData(AbstractBase):
    """Biodata Abstract class."""

    title = models.CharField(max_length=300, null=True, blank=True)
    first_name = models.CharField(max_length=300, null=False, blank=False)
    last_name = models.CharField(max_length=300, null=False, blank=False)
    other_names = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField(max_length=300, null=True, blank=True)
    phone_number = models.CharField(max_length=300, null=True, blank=True)
    date_of_birth =  models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=300, choices=GENDER_CHOICES, null=True, blank=True)
    join_date = models.DateTimeField(default=timezone.now)

    class Meta:
        """Biodata Meta class."""

        abstract = True
