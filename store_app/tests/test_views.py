# from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store_app.models import Category, Product
from store_app.views import store

# @skip("demonstrating skipping")
# class TestSkip(TestCase):
#     def test_skip_exmaple(self):
#         pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                               slug='django-beginners', price='20.00', image='django')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test Product response status
        """
        response = self.c.get(reverse('store1:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test Category response status
        """
        response = self.c.get(reverse('store1:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = store(request)
        html = response.content.decode('utf8')
        print(html)
        self.assertIn('<title> Pkes_Store </title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        """
        Example: Using request factory
        """
        request = self.factory.get('/django-beginners')
        response = store(request)
        html = response.content.decode('utf8')
        self.assertIn('<title> Pkes_Store </title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
