from django.test import TestCase
from rest_framework.test import APIClient

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=50, inventory=100)
        Menu.objects.create(title="Coke", price=80, inventory=100)

    def test_getall(self):
        client = APIClient()
        response = client.get('http://localhost:8000/restaurant/menu/')

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.data, serializer.data)