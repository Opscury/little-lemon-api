from django.urls import path
from .views import BookingDetailView, BookingListCreateView, HomeView, RegistrationView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("api/bookings/", BookingListCreateView.as_view(), name="booking-list"),
    path("api/bookings/<int:pk>/", BookingDetailView.as_view(), name="booking-detail"),
    path("api/registration/", RegistrationView.as_view(), name="registration"),
]
