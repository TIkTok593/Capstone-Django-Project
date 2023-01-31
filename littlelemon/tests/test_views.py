from django.test import TestCase
from restaurant import models

import json

class MenuViewTest(TestCase):
    def test_get_item(self):
        item1 = models.Menu.objects.create(title="Pizza", price=58.89, inventory=23)
        item2 = models.Menu.objects.create(title="Falafel", price=100, inventory=50)
    
    def test_getall(self):
        items = models.Menu.objects.all()
        # self.assertEqual(items, self.item)