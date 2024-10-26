import random
from django.test import TestCase
from django.urls import reverse

from .models import CustomUser

class CustomUserTest(TestCase):
    def setUp(self) -> None: 
        self.user = CustomUser.objects.create_user(
            first_name = "Mary",
            last_name ="Doe",
            email = "marydoe@gmail.com",
            password = "testing321",
            is_buyer =  True,
            is_seller = False
        )
        self.user.save()

    def test_sign_up(self) -> bool:
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@gmail.com",
            "password": "testing321",
            "is_buyer": random.choices([True, False]),
            "is_seller": random.choices([True, False]),
        }
        route = reverse('users:create-users-path')
        response = self.client.post(route, data=user_data, format='json')

        assert response.status_code == 201
    
    def test_sign_in(self) -> bool:
        user_data = {
            "email": "marydoe@gmail.com",
            "password": "testing321"
        }
        route = reverse('users:login-users-path')
        response = self.client.post(route, data=user_data, format='json')
    
        assert response.status_code == 200
    