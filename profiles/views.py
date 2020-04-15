from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Profile
from .permissions import IsOwnerOrAdminOrReadOnly
from .serializers import ProfileSerializer


class ProfileListCreateView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Set read only field 'owner' to the logged in user"""
        user = self.request.user
        serializer.save(owner=user)


class ProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]
