from django.test import TestCase
from cult.models import Item

"""
To run these tests execute in terminal (while in project directory): python manage.py test cult.tests.db_tests
if you want more info - use "verbosity", e.g. : python manage.py test --verbosity=2 cult.tests.db_tests
"""


class ItemDBTests(TestCase):
    def setUp(self):
        Item.objects.create(
            title='Test film',
            received_likes=0
        )

    def test_item_exists(self):
        """ Check if created item exists in database """
        item = Item.objects.get(title='Test film')
        self.assertEqual(item.received_likes, 0)

# class UserDBTests(TestCase): TODO
