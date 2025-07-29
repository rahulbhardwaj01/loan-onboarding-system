from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Loan
from .transformer import transform_loan_data

# directly talken from documentation:

# post check for endpoint
class LoanAPITests(APITestCase):
    def test_create_loan(self):
        url = reverse('loan-create')
        data = {
            "amount": "50000.00",
            "term": 36,
            "customers": [
                {
                    "first_name": "Kyojuro",
                    "last_name": "Rengoku",
                    "email": "rengoku@gmail.com",
                    "address": {
                        "street": "123",
                        "city": "Chandigarh",
                        "state": "Chandigarh",
                        "zip_code": "12345"
                    }
                }
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Loan.objects.count(), 1)
        self.assertEqual(Loan.objects.get().customers.first().first_name, 'Kyojuro')

# transformation checkk:
    def test_json_transformation(self):
        sample_data = {
            "loan_number": "a1b2c3d4-e5f6-a7b8-c9d0-e1f2a3b4c5d6",
            "amount": "1000.00",
            "term": 12,
            "customers": [{
                "first_name": "zenitsu",
                "last_name": "agatsuma",
                "email": "zenith@gmail.com",
                "address": { "street": "123", "city": "chandigarh", "state": "chandigarh", "zip_code": "12345" }
            }]
        }
        transformed = transform_loan_data(sample_data)
        self.assertIsNotNone(transformed)
        self.assertEqual(transformed['loanId'], 'a1b2c3d4-e5f6-a7b8-c9d0-e1f2a3b4c5d6')
        self.assertEqual(transformed['borrower']['fullName'], 'zenitsu agatsuma')