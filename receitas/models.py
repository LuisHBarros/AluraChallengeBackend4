from django.db import models
from datetime import date

class Receita(models.Model):
    descricao = models.CharField(max_length=255, null=False, unique_for_month="data")
    valor = models.FloatField(null=False, default='0.00')
    data = models.DateField(null = False)
    def __str__(self):
        return self.descricao
    

    
