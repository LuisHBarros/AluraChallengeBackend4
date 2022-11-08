from django.db import models

# Create your models here.
class Despesa(models.Model):
    CATEGORIAS = (
        ('a', 'Alimentação'),
        ('s', 'Saúde'),
        ('m', 'moradia'),
        ('t', 'Transporte'), 
        ('e', 'Educação'),
        ('l', 'Lazer'),
        ('i', 'Imprevistos'),
        ('o', 'Outras'))
    descricao = models.CharField(max_length=255, null=False, unique_for_month="data")
    valor = models.FloatField(null=False, default='0.00')
    categoria = models.CharField(null = True, choices=CATEGORIAS, default='o', max_length=1)
    data = models.DateField(null = False)
    
    def __str__(self):
        return self.descricao
