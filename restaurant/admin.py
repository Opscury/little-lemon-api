from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "no_of_guests", "booking_date", "created_by")
    list_filter = ("booking_date",)
    search_fields = ("name", "created_by__username")
