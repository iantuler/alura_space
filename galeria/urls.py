from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
   path('', index, name='casinha'),
   path('imagem/', imagem, name='foto'),
   ]