from django.contrib import admin
from .models import Genero, Filme
from rest_framework.authtoken.models import Token

# Admin para o modelo Generos: mostra o campo 'nome' e permite busca por nome
@admin.register(Genero)
class GenerosAdmin(admin.ModelAdmin):
   list_display = ['nome']
   search_fields = ['nome']


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
  list_display = ['titulo', 'descricao', 'ano_lancamento', 'duracao']  # colunas na listagem
  search_fields = ['titulo', 'ano_lancamento']                            # campos pesquisáveis
  list_filter = ['titulo']  

admin.site.register(Token)