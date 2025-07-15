from django.db import models
from datetime import datetime

class Produto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=100)
    data_validade = models.DateField()
    quantidade = models.PositiveIntegerField()
    data_fabricacao = models.DateField(default=datetime.now)
    lote = models.CharField(max_length=50, blank=True, null=True)
    
    def vencido(self):
        return self.data_validade < datetime.now().date()
    def perto_vencer(self):
        return (self.data_validade - datetime.now().date()).days <= 30
    def __str__(self):
        return f"{self.nome} (Código: {self.codigo}) - Vencimento: {self.data_validade.strftime('%d/%m/%Y')}"


class Armazem(models.Model):
    livre = models.BooleanField(default=True)
    rua = models.CharField(max_length=100)
    predio = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)
    apartamento = models.CharField(max_length=100)

    def __str__(self):
        return f"Rua: {self.rua}, Prédio: {self.predio}, Nível: {self.nivel}, Apartamento: {self.apartamento if self.apartamento else 'N/A'}"
    
class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    armazem = models.ForeignKey(Armazem, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade} unidades em {self.armazem}"