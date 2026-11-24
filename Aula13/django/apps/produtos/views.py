from django.views.generic import ListView
from .models import Categoria, Cliente, Pedido, Produto


class ProdutoListView(ListView):
    #'model': informa ao Django qual tabela do banco de dados será consultada.
    model = Produto

    #'template_name': Caminho do arquivo HTML que  vai receber os dados e renderizar a tela.
    template_name = "produtos/lista_produtos.html"

    context_object_name = "produtos"

    queryset = Produto.objects.select_related("categoria")


class ClienteListView(ListView):
    #'model': informa ao Django qual tabela do banco de dados será consultada.
    model = Cliente

    #'template_name': Caminho do arquivo HTML que  vai receber os dados e renderizar a tela.
    template_name = "produtos/lista_clientes.html"

    context_object_name = "clientes"

    #queryset = Cliente.objects.select_related("")

class CategoriaListView(ListView):
    #'model': informa ao Django qual tabela do banco de dados será consultada.
    model = Categoria

    #'template_name': Caminho do arquivo HTML que  vai receber os dados e renderizar a tela.
    template_name = "produtos/lista_categoria.html"

    context_object_name = "categorias"

    #queryset = Categoria.objects.select_related("")