from rest_framework.test import APITestCase
from rest_framework import status
from .models import Condition
from .serializers import ConditionSerializer


class ConditionTestCase(APITestCase):

    def test_post_condition(self):
        data = {"name": "flue", "state": "CO"}
        response = self.client.post('/conditions/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_conditions(self):
        response = self.client.get("/conditions/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
