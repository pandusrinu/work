from django.test import TestCase
from rest_framework import status
from .models import Product
from rest_framework.test import APITestCase


class ProductTestCase(APITestCase):
    def testcase(self):
        data = {
            "Name": "pepsi",
            "item_cost": 250,
            "stock_quantity": 8

        }

        volume_test = int(data['item_cost'])*int(data['stock_quantity'])
        response = self.client.post("/product/", data)
        volume = response.data['details']['volume']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(volume_test, volume)