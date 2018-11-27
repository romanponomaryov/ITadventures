from django.test import TestCase, Client
from cult.models import Item, User
from django.urls import reverse

"""
Tests for views
"""

# To run these tests execute in terminal (while in project directory): python manage.py test cult.tests.views_tests
# if you want more info - use "verbosity", e.g. : python manage.py test --verbosity=2 cult.tests.views_tests


class IndexViewTests(TestCase):
    """ Tests for homepage """
    def setUp(self):
        client = Client()

    def test_item_liked(self):
        """ Check if the test item is present on index page and can receive a like """
        Item.objects.create(
            title='Test film',
            received_likes=0
        )
        item = Item.objects.get(title='Test film')
        response = self.client.post(f'/{item.id}')
        self.assertEqual(response.status_code, 302)


class TopItemsViewTests(TestCase):
    """ Tests for top 10 films page """
    def setUp(self):
        """ create client and 11 films """
        client = Client()
        for i in range(0, 11):
            item = Item.objects.create(
                title=f'Test film {i}',
                received_likes=i+1
            )
            item.save()

    def test_only_top_items_shown(self):
        """ Check that the film with 11th rank in likes is not present on page """
        response = self.client.get(reverse('top_items'))
        self.assertNotContains(response, 'Test film 0')

    def test_top_items_always_shown(self):
        """ Check that the film with 10th rank in likes is present on page """
        item = Item.objects.get(title='Test film 0')
        item.received_likes += 1
        item.save()
        response = self.client.get(reverse('top_items'))
        self.assertContains(response, 'Test film 0')


class ActivityTests(TestCase):
    """ Tests for user activity page """
    def setUp(self):
        """ create client and 11 users """
        client = Client()
        for i in range(0, 11):
            user = User.objects.create(
                name=f'Test User {i}',
                posted_likes=i
            )
            user.save()

    def test_all_users_always_shown(self):
        """ Check that all users with correct likes value are present on page """
        for i in range(0, 11):
            response = self.client.get(reverse('activity'))
            self.assertContains(response, f'Test User {i} - posted: {i} like(s)')


# class LoginTests(TestCase):

# class LogoutTests(TestCase):


# TODO:
"""
    - index page - when auth is implemented - check for authed ("like" option enabled) and non-authed
    - users activity page +++
    - creation of user - ?
    - user login
    - user logout
"""
