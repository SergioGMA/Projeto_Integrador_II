import json
from vacina.serializers import ProfileSerializer
from vacina.models import Profile

from django.contrib.auth.models import User
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from vacina.api import VacinaViewSet, BannerViewSet, ProfileViewSet, LoginView
from rest_framework.response import Response
from django.test import Client
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ProfileViewSetTestCase(APITestCase):
    @classmethod
    def setUpTestData(self):
        self.username = 'Juliana'
        self.password = '12345'
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

    def test_registration(self):
        data = {
                "id": "1",
                "username": "Ju",
                "first_name": "Juliana",
                "last_name": "Souza",
                "endereco": "ABC",
                "telefone": "813779",
                "email": "ju@gmail.com",
                "cidade": "Gma",
                "comorbidade": "Não",
                "alergia": "Não",
                "cpf": "13038691240",
                "password": "12345"
        }
        response = self.client.post("/api/profile/", data)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# class ProfileViewSetTestCase(APITestCase):

#     list_url = reverse("api")
#     @classmethod
#     def setUp(self):
#         self.user = User.objects.create_user(username='testename', password= "teste123456")
#         self.token = Token.objects.create(user=self.user)
#         self.api_authentication()

#     def api_authentication(self):
#         self.client.credentials(HTTP_AUTHORIZATION="Token" + self.token.key)

#     def test_profile_list_authentication(self):
#         response = self.client.get(self.list_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_profile_list_authentication(self):
#         self.client.force_authenticate(user=None)
#         response = self.client.get(self.list_url)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

