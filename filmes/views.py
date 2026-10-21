from .models import Filme, Genero
from .serializers import FilmesSerializer, GenerosSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class GenerosViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()         # queryset base usado pelo ViewSet
    serializer_class = GenerosSerializer     # serializer que define representação e validação


class FilmesViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()         # queryset base para operações do ViewSet
    serializer_class = FilmesSerializer     # serializer usado para livros
    filter_backends = [DjangoFilterBackend]  # habilita filtragem via django-filter
    # campos permitidos para filtragem via query string, ex: ?titulo=foo or ?autor__nome=Silva
    filterset_fields = ['titulo', 'descricao', 'ano_lancamento']
