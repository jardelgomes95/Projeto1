from django.urls import path

from .views import avaliacaoCreateView, treinoCreateView, ficha_de_saudeCreateView, objetivosCreateView, \
    personalUpdateView, avaliacaoUpdateView
from .views import avaliacaoObsFormView, ficha_de_saudeObsFormView, objetivosObsFormView, medicamentoObsFormView, \
    nutricaoObsFormView
from .views import ficha_de_saudeListView, ficha_de_saudeUpdateView, objetivosUpdateView, objetivosListView, \
    medicamentoListView, medicamentoUpdateView
from .views import medicamentoCreateView, nutricaoCreateView, avaliacaoListView, treinoListView, personalCreateView, \
    personalListView, treinoUpdateView
from .views import nutricaoUpdateView, nutricaoListView, avaliacaoPDFDetailView, avaliacaoDetailView

urlpatterns = [
    path('avaliacao/aluno', avaliacaoCreateView.as_view(), name="Avaliação_Física"),
    path('listar/aluno', avaliacaoListView.as_view(), name="Lista_de_avaliacao"),
    path('atualizar/aluno/<int:pk>', avaliacaoUpdateView.as_view(), name="Atualizar_Aluno"),
    path('atualizar/aluno/observacao/<int:pk>', avaliacaoObsFormView.as_view(), name="Atualizar_obs_aluno"),
    path('pdf/aluno/<int:pk>', avaliacaoPDFDetailView.as_view(), name="pdf_aluno"),
    path('detalhar/aluno/<int:pk>', avaliacaoDetailView.as_view(), name="Detalhar_aluno"),

    path('avaliacao/treino', treinoCreateView.as_view(), name="Cadastrar_Treino"),
    path('listar/treino', treinoListView.as_view(), name="Lista_de_treinos"),
    path('atualizar/treino/<int:pk>', treinoUpdateView.as_view(), name="Atualizar_treino"),

    path('avaliacao/saude', ficha_de_saudeCreateView.as_view(), name="Ficha_de_saúde"),
    path('listar/saude', ficha_de_saudeListView.as_view(), name="Lista_de_saúde"),
    path('atualizar/saude/<int:pk>', ficha_de_saudeUpdateView.as_view(), name="Atualizar_saúde"),
    path('atualizar/saude/observacao/<int:pk>', ficha_de_saudeObsFormView.as_view(), name="Atualizar_obs_saúde"),

    path('avaliacao/objetivos', objetivosCreateView.as_view(), name="Objetivos_do_aluno"),
    path('listar/objetivos', objetivosListView.as_view(), name="Listar_objetivos"),
    path('atualizar/objetivos/<int:pk>', objetivosUpdateView.as_view(), name="Atualizar_objetivos"),
    path('atualizar/objetivos/observacao/<int:pk>', objetivosObsFormView.as_view(), name="Atualizar_obs_objetivos"),

    path('avaliacao/medicamento', medicamentoCreateView.as_view(), name="Medicamentos_usados"),
    path('listar/medicamento', medicamentoListView.as_view(), name="Listar_medicamento"),
    path('atualizar/medicamento/<int:pk>', medicamentoUpdateView.as_view(), name="Atualizar_medicamento"),
    path('atualizar/medicamento/observacao/<int:pk>', medicamentoObsFormView.as_view(), name="Atualizar_obs_medicamento"),

    path('avaliacao/nutricao', nutricaoCreateView.as_view(), name="Nutricao"),
    path('listar/nutricao', nutricaoListView.as_view(), name="Listar_nutricao"),
    path('atualizar/nutricao/<int:pk>', nutricaoUpdateView.as_view(), name="Atualizar_nutricao"),
    path('atualizar/nutricao/observacao/<int:pk>', nutricaoObsFormView.as_view(), name="Atualizar_obs_nutricao"),

    path('avaliacao/personal', personalCreateView.as_view(), name="Cadastrar_Personal"),
    path('listar/personal', personalListView.as_view(), name="Listar_Personal"),
    path('atualizar/personal/<int:pk>', personalUpdateView.as_view(), name="Atualizar_Personal")




]
