from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from receitas.models import Receita
from despesas.models import Despesa
from rest_framework import viewsets, filters, generics

# Create your views here.
class Resumo(APIView):
    def get(self, request, ano, mes):
        ano = self.kwargs['ano']
        mes = self.kwargs['mes']
        total_receitas = self.total_receitas(ano, mes)
        total_despesas = self.total_despesas(ano, mes)
        saldo = total_receitas - total_despesas
        total_gasto_categoria = self.total_gasto_categoria(ano, mes)
        return Response(data={
            "total_receitas": total_receitas,
            "total_despesas": total_despesas,
            "total_gasto_categoria": total_gasto_categoria,
            "saldo" : saldo
        }, status=status.HTTP_200_OK)
        
    def total_receitas(self,ano, mes):
        receitas = Receita.objects.filter(data__year=ano, data__month=mes)
        valor = 0.00
        for receita in receitas:
            valor += receita.valor
        return valor
    
    def total_despesas(self,ano, mes):
        despesas = Despesa.objects.filter(data__year=ano, data__month=mes)
        valor = 0.00
        for despesa in despesas:
            valor += despesa.valor
        return valor
    
    def total_gasto_categoria(self, ano, mes):
        despesas = Despesa.objects.filter(data__contains="{}-{}".format(ano, mes))
        categorias = self.get_dict_categorias()
        for row in despesas:
            categorias[row.categoria] += row.valor
            print(row)
        return categorias
    
    def get_dict_categorias(self) -> dict:
        return {
            "a": 0.00,
            "s": 0.00,
            "m": 0.00,
            "t": 0.00,
            "e": 0.00,
            "l": 0.00,
            "i": 0.00,
            "o": 0.00
        }
    
    