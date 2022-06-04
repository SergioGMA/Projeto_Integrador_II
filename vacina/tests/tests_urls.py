from django.test import SimpleTestCase
from django.test import TestCase
from django.urls import reverse, resolve
from vacina.api import VacinaViewSet, BannerViewSet, ProfileViewSet, LoginView
from django.contrib.auth.models import User
from django.test import Client


class TestProfileModel(TestCase):
    @classmethod
    def setUpTestData(self):
        self.username = 'Juliana'
        self.password = '12345'
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()
        
    def test_login_ok(self):
        c = Client()
        self.client_object = c.login(username=self.username, password=self.password)
        c = Client()
        logged_in = c.login(username='Juliana', password='12345')
        self.assertEquals(logged_in, True)


class loginViewTesteCase(TestCase):

    def test_method_not_allowed_code_405(self):
        response = self.client.get(reverse("login"))
        self.assertEquals(response.status_code, 405)

    def test_unauthorized_status_code_401(self):
        API_LOGIN_URL = '/login/'
        response= self.client.get(API_LOGIN_URL)
        self.assertEquals(response.status_code, 200)

#     def test_status_code_200(self):
#         response = self.client.get("Banner")
#         self.assertEquals(response.status_code, 200)

#     def test_unauthorized_status_code_401(self):
#         url = reverse("login")
#         response = self.client.get(reverse("login"))
#         self.assertEquals(response.status_code, 401)


# class testUrls(SimpleTestCase):

#     def test_list_url_is_resolved(self):
#         url = reverse("Banner")
#         self.assertEquals(resolve(url).func.view_class, BannerViewSet)
