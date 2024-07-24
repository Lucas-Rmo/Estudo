from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
    path('', Listar_Contato.as_view(),name="Listar_contatos"),
    path("novo/", Criar_Contato.as_view(),name = "contato_create"),
    path("editar/<int:pk>/",Atualizar_Contato.as_view(),name="contato_update"),
    path("excluir/<int:pk>/",Deletar_Contato.as_view(),name="contato_delete"),
    path("detalhes/<int:pk>", detalhes_contato,name="detalhes_contato"),

]


