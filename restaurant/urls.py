from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookingViewSet, HomeView, MenuViewSet, RegistrationView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("api/menu-items/", MenuViewSet.as_view({"get": "list", "post": "create"}), name="menu-list"),
    path("api/menu-items/<int:pk>/", MenuViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="menu-detail"),
    path("api/bookings/", BookingViewSet.as_view({"get": "list", "post": "create"}), name="booking-list"),
    path("api/bookings/<int:pk>/", BookingViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="booking-detail"),
    path("api/booking/", BookingViewSet.as_view({"get": "list", "post": "create"}), name="booking-list-legacy"),
    path("api/booking/<int:pk>/", BookingViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="booking-detail-legacy"),
    path("api/registration/", RegistrationView.as_view(), name="registration"),
    path("api-token-auth/", obtain_auth_token, name="api-token-auth"),
    path("api-auth/", include("rest_framework.urls")),
]
