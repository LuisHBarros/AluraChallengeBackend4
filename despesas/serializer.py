from rest_framework import serializers
from despesas.models import Despesa

class DespesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'