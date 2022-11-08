from django.contrib import admin

from despesas.models import Despesa

# Register your models here.
class Despesas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data', 'categoria')
    list_display_links = ('id', 'descricao', 'valor', 'data', 'categoria' )
    search_fields = ('descricao',)
    list_per_pate = 10
    
admin.site.register(Despesa, Despesas)