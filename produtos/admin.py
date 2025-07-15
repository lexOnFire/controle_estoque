from django.contrib import admin
from .models import Produto, Armazem, Estoque




@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'data_validade', 'quantidade', 'vencido', 'perto_vencer')
    search_fields = ('nome', 'codigo')
    list_filter = ('data_validade', 'quantidade')

@admin.register(Armazem)
class ArmazemAdmin(admin.ModelAdmin):
    list_display = ('rua', 'predio', 'nivel', 'apartamento', 'livre')
    search_fields = ('rua', 'predio', 'nivel')
    list_filter = ('livre',)

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('produto', 'armazem', 'quantidade')
    search_fields = ('produto__nome', 'armazem__rua')
    list_filter = ('produto', 'armazem')
