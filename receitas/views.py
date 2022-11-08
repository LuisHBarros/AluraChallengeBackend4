from rest_framework import viewsets, filters, generics
from receitas.models import Receita
from receitas.serializer import ReceitasSerializer
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

class ReceitasViewSet(viewsets.ModelViewSet):
    """Lista todas as receitas cadastradas"""
    queryset = Receita.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    serializer_class = ReceitasSerializer
    search_fields = ['descricao', 'id']

class ReceitasPorMes(generics.ListAPIView):
    def get_queryset(self):
        ano = self.kwargs['ano']
        mes = self.kwargs['mes']
        queryset = Receita.objects.filter(data__year=ano, data__month=mes)
        return queryset
    serializer_class = ReceitasSerializer
    

# class DespesasViewSet(viewsets.ModelViewSet):
#     """Lista todas as despesas cadastradas"""
#     queryset = Despesa.objects.all()
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     serializer_class = DespesasSerializer
#     search_fields = ['descricao', 'id']

# class DespesasPorMes(generics.ListAPIView):
#     def get_queryset(self):
#         queryset = Despesa.objects.filter(ano=self.kwargs['ano'], mes=self.kwargs['mes'])
#         return queryset
#     serializer_class = ListaDespesasPorMes
    
# class ResumoMes(generics.ListAPIView):
#     def get_queryset(self):
#         queryset = Despesa.objects.filter(ano=self.kwargs['ano'], mes=self.kwargs['mes']), Receita.objects.filter(ano=self.kwargs['ano'], mes=self.kwargs['mes'])
#         return queryset
#     serializer_class = ResumoSerializer