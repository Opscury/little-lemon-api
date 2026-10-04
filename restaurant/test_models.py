from decimal import Decimal
from django.test import TestCase
from .models import Menu


class MenuModelTests(TestCase):
    def test_menu_item_is_saved_and_rendered_as_its_title(self):
        item = Menu.objects.create(title="Greek Salad", price=Decimal("12.99"), inventory=7)
        self.assertEqual(str(item), "Greek Salad")
        self.assertEqual(Menu.objects.count(), 1)
