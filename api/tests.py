from unittest import TestCase


# from django.test import TestCase

# Create your tests here.


def tow_sum(a, b):
    return a + b


class TestSum(TestCase):
    def test_sun(self):
        self.assertEqual(tow_sum(1, 2), 3)
