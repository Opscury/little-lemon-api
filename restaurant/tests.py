from datetime import timedelta
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from .models import Booking


class BookingApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("ada", password="secure-pass-123")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.payload = {"name": "Ada Lovelace", "no_of_guests": 2, "booking_date": (timezone.now() + timedelta(days=1)).isoformat()}

    def test_authenticated_user_can_create_and_list_own_bookings(self):
        self.assertEqual(self.client.post(reverse("booking-list"), self.payload, format="json").status_code, 201)
        response = self.client.get(reverse("booking-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_user_cannot_access_another_users_booking(self):
        other = User.objects.create_user("grace", password="secure-pass-123")
        booking = Booking.objects.create(created_by=other, **self.payload)
        self.assertEqual(self.client.get(reverse("booking-detail", args=[booking.pk])).status_code, 404)

    def test_registration_returns_an_authentication_token(self):
        self.client.credentials()
        response = self.client.post(reverse("registration"), {"username": "newuser", "email": "new@example.com", "password": "new-secure-password"}, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertIn("token", response.data)
