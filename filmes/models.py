from django.db import models

# Create your models here.
class Genero(models.Model):
   nome = models.CharField(max_length=255)  # nome do autor

   def __str__(self):
       return self.nome  # representação em string do autor

   class Meta:
       verbose_name = 'Gênero'
       verbose_name_plural = 'Gêneros'

# Create your models here.
class Filme(models.Model):
   titulo = models.CharField(max_length=255)           # título do livro
   descricao = models.CharField(max_length=255)           # título do livro
   ano_lancamento = models.PositiveIntegerField()                  # ano de publicação (positivo)
   genero = models.ForeignKey(Genero, on_delete=models.CASCADE)  # relacionamento com Autor
   duracao = models.CharField(max_length=20)               # código ISBN            # número de páginas (positivo)
   
   def __str__(self):
       return self.titulo  # representação em string do livro

   class Meta:
       verbose_name = 'Filme'
       verbose_name_plural = 'Filmes'
