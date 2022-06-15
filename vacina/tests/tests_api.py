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
        #print(response)
        self.assertEquals(response.status_code, 200)
