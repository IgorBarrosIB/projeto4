from rest_framework import serializers  # ferramentas do DRF transformar a tabela em JSON
from .models import Filme, Genero      # modelos usados pelos serializers

class GenerosSerializer(serializers.ModelSerializer):
   class Meta:
       model = Genero
       fields = '__all__'  # expõe todos os campos do modelo Autor

class FilmesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Filme
       fields = '__all__'  # expõe todos os campos do modelo Livro
