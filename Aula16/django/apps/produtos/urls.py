##
# App - Produto - urls.py
##
from django.urls import path

# CategoriasListarView, ClientesListarView, PedidosListarView,ProdutosListarView,
from .views import (
    ProdutosListView,
    ProdutosDetailView,
    ProdutoDeleteView,
    ProdutoCreateView,


)

app_name = "produtos"

urlpatterns = [
    path("", ProdutosListView.as_view(), name="lista"),
    path("itens/", ProdutosListView.as_view(), name="produtos_listar"),
    path("itens/<int:pk>/", ProdutosDetailView.as_view(), name="detalhes"),
    path("itens/<int:pk>/delete/", ProdutoDeleteView.as_view(), name="remover"),
    path("itens/adicionar/", ProdutoCreateView.as_view(), name="adicionar")
    #path("listar/", ProdutosListarView.as_view(), name="produtos_listar"),
    #path("categorias/", CategoriasListarView.as_view(), name="categorias_listar"),
    #path("clientes/", ClientesListarView.as_view(), name="clientes_listar"),
    #path("pedidos/", PedidosListarView.as_view(), name="pedidos_listar"),
]
