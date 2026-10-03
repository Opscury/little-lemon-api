from django.conf import settings
from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField()
    booking_date = models.DateTimeField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")

    class Meta:
        ordering = ["booking_date"]

    def __str__(self):
        return f"{self.name} — {self.booking_date:%Y-%m-%d %H:%M}"
