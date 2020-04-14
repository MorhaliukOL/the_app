from django.urls import path
from .views import ProfileListCreateView, ProfileDetailView

urlpatterns = [
    path("list/", ProfileListCreateView.as_view(), name="all-profiles"),
    path("<int:pk>/", ProfileDetailView.as_view(), name="profile"),
]