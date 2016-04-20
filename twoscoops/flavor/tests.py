__author__ = 'plevytskyi'
from django.test import TestCase


class FooTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one_equals_one(self):
        self.assertEqual(1, 1)