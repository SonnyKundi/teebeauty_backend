"""Provider's models file."""

from tersun.common.models import BioData
from django.db import models
from tersun.common.utils import get_directory

class Provider(BioData):
    """Provider models."""

    provider_number = models.CharField(max_length=300, null=True, blank=True)
    profile_image = models.FileField(upload_to=get_directory)

    def __str__(self) -> str:
        return self.first_name +" " + self.other_names + " " + self.last_name + " " + self.provider_number