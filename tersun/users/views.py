"""Users views file."""

from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from tersun.users.models import User
from tersun.users import filters, serializers


class UserViewSet(viewsets.ModelViewSet):
    """User Viewset class."""

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filterset_class = filters.UserFilter
    search_fields = (
        'first_name', 'last_name', 'other_names', 'username', 'user_type',
        'phone_number', 'email', 'date_of_birth', 'join_date')


class MeView(RetrieveAPIView):
    """Return the details of the currently logged in user."""

    permission_classes = (IsAuthenticated,)
    queryset = User.objects.none()
    serializer_class = serializers.MeSerializer

    def get_object(self):
        """Limit this view to only return the logged in user's details."""
        return self.request.user
