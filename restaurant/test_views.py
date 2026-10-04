from decimal import Decimal
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from .models import Menu


class ApiViewSetTests(APITestCase):
    def test_menu_endpoint_is_browsable_and_returns_menu_items(self):
        Menu.objects.create(title="Lemon Cake", price=Decimal("5.00"), inventory=3)
        response = self.client.get("/api/menu-items/", HTTP_ACCEPT="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["title"], "Lemon Cake")

    def test_booking_endpoint_requires_a_token(self):
        response = self.client.get("/api/bookings/")
        self.assertEqual(response.status_code, 401)

    def test_authenticated_user_can_create_a_booking(self):
        user = User.objects.create_user("mario", password="secure-pass-123")
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
        response = self.client.post("/api/bookings/", {"name": "Mario", "no_of_guests": 3, "booking_date": "2026-10-10T18:30:00Z"}, format="json")
        self.assertEqual(response.status_code, 201)
