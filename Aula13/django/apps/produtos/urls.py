from django.urls import path

from .views import (
    ProdutoListView,
    ClienteListView,
    CategoriaListView,
)

app_name = "produtos"

urlpatterns = [
    path("", ProdutoListView.as_view(), name="lista"),
    path("clientes/", ClienteListView.as_view(), name="listar_cliente"),
    path("categorias/", CategoriaListView.as_view(), name="listar_categoria"),
]