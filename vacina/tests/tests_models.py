from django.test import TestCase
from vacina.models import Banner, Profile, Vacina
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.db import models
from django.test import Client
from django.contrib.auth.models import UserManager


class BannerModelTest(TestCase):

    @classmethod
    def setUpTestData(self):
        self.banner=Banner.objects.create(banner='TESTE DO BANNER')

    def test_retorno_banner(self):
        b1 = Banner.objects.get(banner='TESTE DO BANNER')
        self.assertEquals(b1.__str__(), 'TESTE DO BANNER')

    def test_retorno_banner_label_verbose_name(self):
        b = Banner.objects.get(id=1)
        field_label = b._meta.get_field('banner').verbose_name
        self.assertEquals(field_label, 'Banner')

    def test_retorno_banner_label_default(self):
        b = Banner.objects.get(id=1)
        field_label = b._meta.get_field('banner').default
        self.assertEquals(field_label, 'EM BREVE SERÁ DIVULGADO UMA NOVA CAMPANHA DE VACINAÇÃO')

    def test_retorno_banner_label_max_length(self):
        b = Banner.objects.get(id=1)
        field_label = b._meta.get_field('banner').max_length
        self.assertEquals(field_label, 1000)

        
class TestProfileModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='Juliana', password='12345')
        # u=User.objects.filter(username="Juliana")
        # print(u)

    def test_authenticate_user_success(self):
        """Teste de autenticação com sucesso"""
        user = authenticate(username='Juliana', password='12345')
        self.assertTrue((user is not None) and user.is_authenticated)

        
class VacinaTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(username='Juliana00', password='12345')
        u = User.objects.get(username="Juliana00")
        u.profile.first_name = 'Juliana'
        u.profile.last_name = 'Juliana'
        u.profile.email = 'ju@gmail.com'
        u.profile.cpf = '13038691240'
        u.save()
        
    def test_retorno_profile_email(self):
        p = Profile.objects.all()[0]
        self.assertEquals(p.email, 'ju@gmail.com')
    
    def test_retorno_profile_first_name(self):
        p = Profile.objects.all()[0]
        self.assertEquals(p.first_name, 'Juliana')

    def test_retorno_profile_label_verbose_name(self):
        p = Profile.objects.all()[0]
        field_label = p._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first_name')

