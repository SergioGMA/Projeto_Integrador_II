from importlib.util import source_hash
from rest_framework import serializers
from .models import Vacina, Profile, Banner


class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = [
            'id',
            'user', 
            'vacina', 
            'fabricante', 
            'lote', 
            'dose', 
            'prof',
            'reg_profissional',
            'unidade',
            'data_fabricacao',
            'data_validade',
            ]


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, style={'input_type': 'password'})
    #confirm = serializers.CharField(min_length=8)
    
    class Meta:
        model = Profile
        fields = [
            'id',
            'username', 
            'first_name', 
            'last_name', 
            'endereco', 
            'telefone', 
            'email',
            'cidade',
            'comorbidade', 
            'alergia', 
            'cpf',
            'password',
            #'confirm'
        ]


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = [
            'id',
            'banner',
        ]