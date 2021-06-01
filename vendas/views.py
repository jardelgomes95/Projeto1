from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from easy_pdf.views import PDFTemplateResponseMixin
from django.contrib import messages
from .forms import *
from .models import matricula, outros_servico, financeiro, pilates, fitdance, kangoodance, funcional, muaythai, \
    frequencia


# Create your views here.

########## CREATEVIEW ##########


class matriculaCreateView(CreateView):
    model = matricula
    template_name = 'cliente.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('Listar_Matricula')


class outros_servicoCreateView(CreateView):
    model = outros_servico
    template_name = 'outros_servicos.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('Listar_Outros_Servicos')


class financeiroCreateView(CreateView):
    model = financeiro
    template_name = 'financeiro.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('Listar_Financeiro')


class pilatesCreateView(CreateView):
    model = pilates
    template_name = 'pilates.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('Listar_Pilates')


class fitdanceCreateView(CreateView):
    model = fitdance
    template_name = 'fit_dance.html'

    fields = '__all__'


class kangoodanceCreateView(CreateView):
    model = kangoodance
    template_name = 'kangoo.html'

    fields = '__all__'


class funcionalCreateView(CreateView):
    model = funcional
    template_name = 'kangoo.html'

    fields = '__all__'


class muaythaiCreateView(CreateView):
    model = muaythai
    template_name = 'muay_thai.html'

    fields = '__all__'


class frequenciaCreateView(CreateView):
    model = frequencia
    template_name = 'frequencia.html'

    fields = '__all__'


########## LISTVIEW ##########


class matriculaListView(ListView):
    model = pilates
    template_name = 'listar/listarpilates.html'
    paginate_by = 10


class financeiroListView(ListView):
    model = financeiro
    template_name = 'listar/listarfinanceiro.html'
    paginate_by = 10


class frequenciaListView(ListView):
    model = frequencia
    template_name = 'listar/listarfrequencia.html'
    paginate_by = 10


class outros_servicosListView(ListView):
    model = outros_servico
    template_name = 'listar/listaroutros_servicos.html'
    paginate_by = 10


class pilatesListView(ListView):
    model = pilates
    template_name = 'listar/listarpilates.html'
    paginate_by = 10


########## UPDATEVIEW ##########


class matriculaUpdateView(UpdateView):
    model = matricula
    template_name = 'cliente.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('Listar_Matricula')


class financeiroUpdateView(UpdateView):
    model = financeiro
    template_name = 'financeiro.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('Listar_Financeiro')


class frequenciaUpdateView(UpdateView):
    model = frequencia
    template_name = 'frequencia.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('Listar_Frequencia')


class outros_servicosUpdateView(UpdateView):
    model = outros_servico
    template_name = 'outros_servicos.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('Listar_Outros_Servicos')


class pilatesUpdateView(UpdateView):
    model = pilates
    template_name = 'pilates.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('Listar_Pilates')


########## FORMS ##########


class matriculaObsForm(UpdateView):
    model = matricula
    form_class = matriculaObsForm
    template_name = 'Atualizar/atualizarcliente.html'

    def get_success_url(self):
        messages.success(self.request, 'Observação atualizada com sucesso!')
        return reverse_lazy('Listar_Matricula')
