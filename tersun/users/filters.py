"""Users filters file."""
from tersun.common.filters import SearchComboboxBaseFilter
from tersun.users import models


class UserFilter(SearchComboboxBaseFilter):
    """Filter individual user user."""

    class Meta:
        """Restrict filter fields."""

        model = models.User
        fields = '__all__'
