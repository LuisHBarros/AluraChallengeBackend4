from django.contrib import admin
from receitas.models import Receita

class Receitas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao', 'valor', 'data')
    search_fields = ('descricao',)
    list_per_pate = 10

admin.site.register(Receita, Receitas)

