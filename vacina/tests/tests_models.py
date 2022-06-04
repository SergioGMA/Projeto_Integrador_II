from django.test import TestCase
from vacina.models import Banner, Profile
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


# class TestProfileModel(TestCase):
    
#     def setUp(self):
#         testuser = User.objects.create_user(username='Juliana', email='ju@gmail.com', password='12345678')
#         #return self.user.username
#         #return User.objects.get(pk=self.user_id)
#         print(testuser)
        
class TestProfileModel(TestCase):
    @classmethod
    def setUpTestData(self):
        self.username = 'Juliana'
        self.password = '12345'
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()
        
        c = Client()
        self.client_object = c.login(username=self.username, password=self.password)

        c = Client()
        logged_in = c.login(username='Juliana', password='12345')
        print(logged_in)
        print(user.id)
        
        self.u = Profile.objects.create(
            #username=('Juliana'),
            #password=('12345'),
            #user="Ju",
            first_name=('Juliana'),
            last_name=('Souza'),
            endereco=('ABC'),
            telefone=('813779'),
            email=('ju@gmail.com'),
            cidade=('Gma'),
            comorbidade=('Não'),
            alergia=('Não'),
            cpf=('13038691240'),
        )
        self.u.save()
        p = Profile.objects.all().values('first_name')
        print(p)
    def test_retorno_profile(self):
        p1 = Profile.objects.get(username='Juliana')
        self.assertEquals(p1.__str__(), 'Juliana')



        # user.profile.username = Profile.objects.create_user('Juliana')
        # user.profile.first_name = Profile.objects.create_user('Juliana')
        # user.profile.last_name = Profile.objects.create_user('Souza')
        # user.profile.endereco = Profile.objects.create_user('ABC')
        # user.profile.telefone = Profile.objects.create_user('813779')
        # user.profile.email = Profile.objects.create_user('ju@gmail.com')
        # user.profile.cidade = Profile.objects.create_user('Gma')
        # user.profile.comorbidade = Profile.objects.create_user('Não')
        # user.profile.alergia = Profile.objects.create_user('Não')
        # user.profile.cpf = Profile.objects.create_user('13038691240')
        
        
    # def post(self, request):
    #     user = User.objects.all().filter(username=request.data['username'])
    #     prof = Profile.objects.all().filter(cpf=request.data['cpf'])

    #     if len(user) == 0 and len(prof) == 0:
    #         u = User.objects.create( username=request.data['username'], password=request.data['password'], )
    #         u.profile.cpf = request.data['cpf']
    #         u.profile.first_name = request.data['first_name']
    #         u.profile.last_name = request.data['last_name']
    #         u.profile.endereco = request.data['endereco']
    #         u.profile.telefone = request.data['telefone']
    #         u.profile.email = request.data['email']
    #         u.profile.cidade = request.data['cidade']
    #         u.profile.comorbidade = request.data['comorbidade']
    #         u.profile.alergia = request.data['alergia']
    #         u.save()

        

#         self.first_name = Profile.objects.create(first_name='Juliana')
#         self.last_name = Profile.objects.create(last_name='Souza')
#         self.endereco = Profile.objects.create(endereco='ABC')
#         self.telefone = Profile.objects.create(telefone='813779,23')
#         self.email = Profile.objects.create(email='ju@gmail.com')
#         self.cidade = Profile.objects.create(cidade='Gma')
#         self.comorbidade = Profile.objects.create(comorbidade='Não')
#         self.alergia = Profile.objects.create(alergia='Não')
#         self.cpf = Profile.objects.create(cpf='13038691240')
        
#         p = Profile.objects.all().values('cpf')
#         print(p)
            
        
#     def test_retorno_profile(self):
#         p1 = Profile.objects.get(first_name='Juliana')
#         self.assertEquals(p1.__str__(), 'Juliana')
        
    #     lista = User.objects.create(first_name=self.first_name, last_name=self.last_name, endereco=self.endereco, telefone=self.telefone, email=self.email, cidade=self.cidade, comorbidade=self.comorbidade, alergia=self.alergia, cpf=self.cpf) 
        
    #     lista.save()
        
    #     print(lista)
    # def test_profile_first_name_users(self):
    #     first_name.likes.set([user.pk])
    #     self.assertEquals(str(self.first_name),"Juliana")