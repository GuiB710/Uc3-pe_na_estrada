"""
MÓDULO: views.py
OBJETIVO:
    Apresentar dados do banco em páginas HTML utilizando as Class-Based Views (CBVs)
    do Django — especificamente a ListView, que serve para listar registros.
"""

# 1. IMPORTAÇÕES DO DJANGO
# A ListView é uma classe pronta do Django que automatiza todo o processo de:
# - Consultar o banco de dados
# - Paginar ou filtrar registros (se necessário)
# - Enviar os dados para um arquivo HTML (template)
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

# 2. IMPORTAÇÕES DOS NOSSOS MODELOS
# Importamos as tabelas/classes definidas no arquivo models.py do mesmo app (.)
from .models import Categoria, Cliente, Pedido, Produto
from .forms import ProdutoForm
from django.urls import reverse_lazy
##
# CBV
# FBV
##
# ==============================================================================
# VIEW 1: Exibição de Produtos em Formato de Cards / Catálogo
# ==============================================================================
class ProdutosListView(ListView):
    # 'model': Informa ao Django qual tabela do banco de dados será consultada.
    model = Produto
    template_name = "produtos/lista_produtos.html"
    context_object_name = "produtos"
    queryset = Produto.objects.select_related("categoria")


# ==============================================================================
# VIEW 2: Exibição de Produtos em Formato de Tabela Administrativa
# ==============================================================================
class ProdutosListarView(ListView):
    # Demonstra a flexibilidade do Django: podemos consultar os mesmos dados (Produto),
    # mas exibi-los em um template visualmente diferente (lista_produtos-tabela.html).
    model = Produto
    template_name = "produtos/lista_produtos-tabela.html"
    context_object_name = "produtos"
    queryset = Produto.objects.select_related("categoria")

class ProdutosDetailView(DetailView):
    model=Produto
    template_name= "produtos/produtos_detail.html"
    context_object_name= "produto"
    queryset= Produto.objects.select_related("categoria")


class ProdutoDeleteView(DeleteView):
    model= Produto
    template_name= "produtos/produtos_confirm_delete.html"
    context_object_name= "produto"
    success_url= reverse_lazy("produtos:produtos_listar")

class ProdutoCreateView(CreateView):
    model= Produto
    form_class= ProdutoForm
    template_name= "produto/produto_form.html"
    success_url= reverse_lazy("produtos:produtos_listar")
# ==============================================================================
# VIEW 3: Listagem de Categorias
# ==============================================================================
class CategoriasListarView(ListView):
    # Modelo a ser listado
    model = Categoria
    # Template HTML que exibirá as categorias cadastradas
    template_name = "produtos/lista_categorias.html"
    # Variável acessível dentro do HTML ({% for categoria in categorias %})
    context_object_name = "categorias"


# ==============================================================================
# VIEW 4: Listagem de Clientes
# ==============================================================================
class ClientesListarView(ListView):
    model = Cliente
    template_name = "produtos/lista_clientes.html"
    context_object_name = "clientes"
    # O modelo Cliente possui uma relação 1-para-1 com o modelo User padrão do Django:
    # usuario = models.OneToOneField(User, ...)
    # O 'select_related("usuario")' faz o JOIN antecipado com a tabela de usuários,
    # permitindo acessar cliente.usuario.username ou cliente.usuario.email no HTML sem queries extras.
    queryset = Cliente.objects.select_related("usuario")

# ==============================================================================
# VIEW 5: Listagem de Pedidos (Consulta Avançada com Múltiplos Relacionamentos)
# ==============================================================================
class PedidosListarView(ListView):
    model = Pedido
    template_name = "produtos/lista_pedidos.html"
    context_object_name = "pedidos"

    # OTIMIZAÇÃO AVANÇADA DE BANCO DE DADOS:
    #
    # 1. select_related("cliente__usuario", "endereco_entrega"):
    #    - Usado para relacionamentos de chave única (ForeignKey ou OneToOne).
    #    - Faz um JOIN SQL direto.
    #    - "cliente__usuario": Navega em cadeia! Traz o Cliente E o Usuário daquele cliente em uma tacada só.
    #    - "endereco_entrega": Traz também os dados do endereço de entrega vinculado ao pedido.
    #
    # 2. prefetch_related("itens"):
    #    - Usado para relacionamentos múltiplos (ManyToMany ou o inverso de uma ForeignKey, 1-para-N).
    #    - Como um Pedido possui muitos itens (Pedido -> ItemPedido), o SQL não resolve isso bem com um simples JOIN.
    #    - O Django faz 2 consultas separadas de alta performance e junta tudo em memória Python,
    #      permitindo acessar 'pedido.itens.all()' no HTML sem disparar novas requisições ao banco.
    queryset = (
        Pedido.objects.select_related("cliente__usuario", "endereco_entrega")
        .prefetch_related("itens")
    )