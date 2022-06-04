from django.contrib import admin
from .models import Vacina, Profile, Banner


@admin.register(Vacina)
class VacinaAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'vacina', 'fabricante', 'lote', 'data_fabricacao', 'dose',
                    'prof', 'reg_profissional', 'unidade', 'data_aplicacao', 'data_validade')
    list_display_links = ('id', 'user', 'vacina', 'fabricante', 'lote', 'data_fabricacao', 'dose',
                        'prof', 'reg_profissional', 'unidade', 'data_aplicacao', 'data_validade')


@admin.register(Profile)
class VacinaAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'cpf', 'endereco', 'telefone', 'email', 'cidade', 'comorbidade', 'alergia',)
    list_display_links = ('id', 'user', 'cpf', 'endereco', 'telefone', 'email', 'cidade', 'comorbidade', 'alergia',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('banner',)


#admin.site.register(Profile)
