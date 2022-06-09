from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from datetime import datetime


class Vacina(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vacina = models.CharField(verbose_name='Vacina',
                              max_length=100, default="Vacina")
    fabricante = models.CharField(
        verbose_name='Fabricante', max_length=100, default="Fabricante")
    lote = models.CharField(verbose_name='lote',
                            max_length=100, default="lote")
    dose = models.CharField(verbose_name='Dose',
                            max_length=100, default="Dose")
    prof = models.CharField(verbose_name='Profissional',
                            max_length=100, default="Profissional")
    reg_profissional = models.CharField(
        verbose_name='Reg Profissional', max_length=100, default="Reg Profissional")
    unidade = models.CharField(
        verbose_name='Unidade', max_length=100, default="Unidade")
    data_aplicacao = models.DateField(
        verbose_name='Data Aplicação', auto_now=True)
    data_fabricacao = models.DateTimeField(
        verbose_name='Data Fabricação', default=datetime.now)
    data_validade = models.DateTimeField(
        verbose_name='Data Validade', max_length=100, default=datetime.now)
        
    def __str__(self):
        return str(self.user)
        


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    first_name = models.CharField(
        verbose_name='first_name', max_length=30, default="Nome")
    last_name = models.CharField(
        verbose_name='last_name', max_length=30, default="Sobrenome")
    endereco = models.CharField(
        verbose_name='Endereço', max_length=50, default="Endereço")
    telefone = models.CharField(
        verbose_name='Telefone', max_length=11, default="Telefone")
    email = models.CharField(
        verbose_name='email', max_length=30, default="email")
    cidade = models.CharField(verbose_name="Cidade",
                              max_length=30, default="Cidade")
    comorbidade = models.CharField(
        verbose_name='Possui Comorbidade?', max_length=10, default="Não")
    alergia = models.CharField(
        verbose_name='Apresenta algum tipo de alergia?', max_length=10, default="Não")
    cpf = models.CharField(verbose_name='CPF', max_length=14, unique=True, null=True)

    def __str__(self):
        return str(self.user)
        #return self.user.get_username()
        #return str(self.first_name + self.last_name)
    

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()


# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if not instance.is_superuser:
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()


def save_user_profile(sender, instance, **kwargs):
    if not instance.is_superuser:
        instance.profile.save()


class Banner(models.Model):
    banner = models.TextField(verbose_name='Banner', max_length=1000,
                              default="EM BREVE SERÁ DIVULGADO UMA NOVA CAMPANHA DE VACINAÇÃO")

    def __str__(self):
        return str(self.banner)