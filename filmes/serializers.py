from rest_framework import serializers  # ferramentas do DRF transformar a tabela em JSON
from .models import Filmes, Generos      # modelos usados pelos serializers

class GenerosSerializer(serializers.ModelSerializer):
   class Meta:
       model = Generos
       fields = '__all__'  # expõe todos os campos do modelo Autor

class FilmesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Filmes
       fields = '__all__'  # expõe todos os campos do modelo Livro
