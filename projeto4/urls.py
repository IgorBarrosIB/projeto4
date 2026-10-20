from django.contrib import admin          
from django.urls import path, include    
from rest_framework.routers import DefaultRouter  
from filmes.views import FilmesViewSet, GenerosViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
# registra endpoints para filmes
router.register(r'filmes', FilmesViewSet)  # registra endpoints para autores: /api/autores/
router.register(r'generos', GenerosViewSet)   # registra endpoints para livros: /api/livros/


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),        # inclui rotas geradas pelo router sob o prefixo /api/
    path('api/token/', obtain_auth_token), 
]
