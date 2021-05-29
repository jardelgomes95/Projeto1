from django.urls import path

from .views import kangoodanceCreateView, funcionalCreateView, muaythaiCreateView, frequenciaCreateView, \
    frequenciaListView, financeiroListView, matriculaUpdateView
from .views import matriculaCreateView, outros_servicoCreateView, financeiroCreateView, pilatesCreateView, \
    fitdanceCreateView, matriculaListView, financeiroUpdateView, frequenciaUpdateView

urlpatterns = [
    path('vendas/aluno', matriculaCreateView.as_view(), name="Matricula"),
    path('vendas/outrosservicos', outros_servicoCreateView.as_view(), name="Outros_Serviços"),
    path('vendas/financeiro', financeiroCreateView.as_view(), name="Financeiro"),
    path('vendas/pilates', pilatesCreateView.as_view(), name="Pilates"),
    path('vendas/fitdance', fitdanceCreateView.as_view(), name="Fitdance"),
    path('vendas/kangoo', kangoodanceCreateView.as_view(), name="Kangoo"),
    path('vendas/funcional', funcionalCreateView.as_view(), name="Funcional"),
    path('vendas/muaythai', muaythaiCreateView.as_view(), name="Muaythai"),
    path('vendas/frequencia', frequenciaCreateView.as_view(), name="Frequencia"),
    path('listar/cliente', matriculaListView.as_view(), name="Listar_Matricula"),
    path('listar/frequencia', frequenciaListView.as_view(), name="Listar_Frequencia"),
    path('listar/financeiro', financeiroListView.as_view(), name="Listar_Financeiro"),


    path('editar/matricula/<int:pk>/', matriculaUpdateView.as_view(), name="Editar_Matricula"),
    path('editar/financeiro/<int:pk>/', financeiroUpdateView.as_view(), name="Editar_Financeiro"),
    path('editar/frequencia/<int:pk>/', frequenciaUpdateView.as_view(), name="Editar_Frequencia"),
]
