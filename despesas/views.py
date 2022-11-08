from rest_framework import viewsets, filters, generics
from despesas.models import Despesa
from despesas.serializer import DespesasSerializer
from django_filters.rest_framework import DjangoFilterBackend

class DespesasViewSet(viewsets.ModelViewSet):
    """Lista todas as despesas cadastradas"""
    queryset = Despesa.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    serializer_class = DespesasSerializer
    search_fields = ['descricao', 'id']

class DespesasPorMes(generics.ListAPIView):
    def get_queryset(self):
        ano = self.kwargs['ano']
        mes = self.kwargs['mes']
        queryset = Despesa.objects.filter(data__year=ano, data__month=mes)
        return queryset
    serializer_class = DespesasSerializer