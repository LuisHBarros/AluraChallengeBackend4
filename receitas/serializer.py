from rest_framework import serializers
from receitas.models import Receita

class ReceitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'
    
        

# class ListaDespesasPorMes(serializers.ModelSerializer):
#     despesa_descricao = serializers.ReadOnlyField(source='descricao')
#     despesa_valor = serializers.ReadOnlyField(source='valor')
#     despesa_dia = serializers.ReadOnlyField(source='dia')
#     despesa_categoria = serializers.ReadOnlyField(source='categoria')
#     class Meta:
#         model = Despesa
#         fields = ['despesa_descricao', 'despesa_valor', 'despesa_dia', 'despesa_categoria']
        
# class ResumoSerializer(serializers.ModelSerializer):
#     receita_valor = serializers.ReadOnlyField(source='valor')
#     # despesas_valor = Despesa.objects.aggregate(Sum('valor'))
#     # saldo_final = receitas_valor.values() - despesas_valor.values()
#     class Meta:
#         model = Receita
#         fields = ['receita_valor']
    