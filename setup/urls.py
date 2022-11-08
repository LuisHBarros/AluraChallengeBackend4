from django.contrib import admin
from django.urls import include, path
from receitas.views import ReceitasViewSet
from rest_framework import routers
from receitas.views import ReceitasPorMes
from despesas.views import DespesasViewSet, DespesasPorMes
from resumo.views import Resumo

router = routers.DefaultRouter()
router.register('receitas', ReceitasViewSet, basename='Receitas')
router.register('despesas', DespesasViewSet, basename='Despesas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('receitas/<int:ano>/<int:mes>', ReceitasPorMes.as_view()),
    path('despesas/<int:ano>/<int:mes>', DespesasPorMes.as_view()),
    path('resumo/<int:ano>/<int:mes>', Resumo.as_view())
]
