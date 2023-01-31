from django.test import TestCase

from restaurant import models

import json

class MenuTest(TestCase):
    def test_get_item(self):
        item = models.Menu.objects.create(title="Pizza", price=58.89, inventory=23)
        self.assertEqual(item.title, "Pizza")
        # self.assertFalse(item.price, 58.89)