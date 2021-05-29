from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from easy_pdf.views import PDFTemplateResponseMixin
from .forms import avaliacaoObsForm, ficha_de_saudeObsForm, objetivosObsForm, medicamentoObsForm, nutricaoObsForm
from .models import avaliacao, ficha_de_saude, treino, objetivos, medicamento, nutricao, personal


# Create your views here.


class avaliacaoCreateView(CreateView):
    model = avaliacao
    template_name = 'aluno.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Avaliação cadastrada com suceso!')
        return reverse_lazy("Lista_de_avaliacao")


class avaliacaoListView(ListView):
    model = avaliacao
    template_name = 'listar/listaraluno.html'
    paginate_by = 10


class avaliacaoUpdateView(UpdateView):
    model = avaliacao
    template_name = 'atualizar/atualizaraluno.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Avaliação atualizada com sucesso!')
        return reverse_lazy('Lista_de_avaliacao')



class avaliacaoObsFormView(UpdateView):
    model = avaliacao
    form_class = avaliacaoObsForm
    template_name = 'atualizar/atualizaraluno.html'

    def get_success_url(self):
        messages.success(self.request, 'Observação atualizada com sucesso!')
        return reverse_lazy('Lista_de_avaliacao')


class avaliacaoDetailView(DetailView):
    model = avaliacao
    template_name = 'detalhar/detalharaluno.html'


class avaliacaoPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = avaliacao
    template_name = 'detalhar/pdfaluno.html'




class ficha_de_saudeCreateView(CreateView):
    model = ficha_de_saude
    template_name = 'saude.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Ficha de Saúde cadastrada com suceso!')
        return reverse_lazy("Lista_de_saúde")


class ficha_de_saudeListView(ListView):
    model = ficha_de_saude
    template_name = 'listar/listarsaude.html'
    paginate_by = 10



class ficha_de_saudeUpdateView(CreateView):
    model = ficha_de_saude
    template_name = 'atualizar/atualizarsaude.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Ficha de Saúde Atualizada com suceso!')
        return reverse_lazy("Lista_de_saúde")


class ficha_de_saudeObsFormView(UpdateView):
    model = ficha_de_saude
    form_class = ficha_de_saudeObsForm
    template_name = 'atualizar/atualizarsaude.html'

    def get_success_url(self):
        messages.success(self.request, 'Observação atualizada com sucesso!')
        return reverse_lazy('Lista_de_saúde')



class treinoCreateView(CreateView):
    model = treino
    template_name = 'treino.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Treino cadastrado com suceso!')
        return reverse_lazy("Lista_de_treinos")


class treinoListView(ListView):
    model = treino
    template_name = 'listar/listartreino.html'
    paginate_by = 5


class treinoUpdateView(UpdateView):
    model = treino
    template_name = 'atualizar/atualizartreino.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Treino atualizado com sucesso!')
        return reverse_lazy('Lista_de_treinos')



####################################################################################################


class objetivosCreateView(CreateView):
    model = objetivos
    template_name = 'objetivos.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Objetivos cadastrados com suceso!')
        return reverse_lazy("Listar_objetivos")

class objetivosListView(ListView):
    model = objetivos
    template_name = 'listar/listarobjetivos.html'
    paginate_by = 10


class objetivosUpdateView(UpdateView):
    model = objetivos
    template_name = 'atualizar/atualizarobjetivos.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Ficha de Saúde Atualizada com suceso!')
        return reverse_lazy("Listar_objetivos")


class objetivosObsFormView(UpdateView):
    model = objetivos
    form_class = objetivosObsForm
    template_name = 'atualizar/atualizarobjetivos.html'

    def get_success_url(self):
        messages.success(self.request, 'Observação atualizada com sucesso!')
        return reverse_lazy('Listar_objetivos')

#######################################################################################################


class medicamentoCreateView(CreateView):
    model = medicamento
    template_name = 'medicamento.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Medicamentos usados cadastrados com suceso!')
        return reverse_lazy("Listar_medicamento")


class medicamentoListView(ListView):
    model = medicamento
    template_name = 'listar/listarmedicamento.html'
    paginate_by = 10


class medicamentoUpdateView(CreateView):
    model = medicamento
    template_name = 'atualizar/atualizarmedicamento.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Ficha de Medicamentos usados Atualizada com suceso!')
        return reverse_lazy("Listar_medicamento")



class medicamentoObsFormView(UpdateView):
    model = medicamento
    form_class = medicamentoObsForm
    template_name = 'atualizar/atualizarmedicamento.html'

    def get_success_url(self):
        messages.success(self.request, 'Observação atualizada com sucesso!')
        return reverse_lazy('Listar_medicamento')


##############################################################################################



class nutricaoCreateView(CreateView):
    model = nutricao
    template_name = 'nutricao.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Ficha nutricional cadastrada com suceso!')
        return reverse_lazy("Listar_nutricao")

class nutricaoListView(ListView):
    model = nutricao
    template_name = 'listar/listarnutricao.html'
    paginate_by = 10



class nutricaoUpdateView(CreateView):
    model = nutricao
    template_name = 'atualizar/atualizarnutricao.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Ficha de Nutrição Atualizada com suceso!')
        return reverse_lazy("Listar_nutricao")


class nutricaoObsFormView(UpdateView):
    model = nutricao
    form_class = nutricaoObsForm
    template_name = 'atualizar/atualizarnutricao.html'

    def get_success_url(self):
        messages.success(self.request, 'Observação atualizada com sucesso!')
        return reverse_lazy('Listar_nutricao')


#################################################################################################


class personalCreateView(CreateView):
    model = personal
    template_name = 'personal.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Personal Cadastrado com sucesso!')
        return reverse_lazy('Listar_Personal')

class personalListView(ListView):
    model = personal
    template_name = 'listar/listarpersonal.html'
    paginate_by = 5



class personalUpdateView(UpdateView):
    model = personal
    template_name = 'atualizar/atualizarpersonal.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Personal atualizado com sucesso!')
        return reverse_lazy('Listar_Personal')