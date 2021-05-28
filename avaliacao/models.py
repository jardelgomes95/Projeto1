from django.db import models
# Create your models here.

class avaliacao(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Não Quero Informar")
    )
    nome = models.CharField(max_length=64, null=False, blank=False, verbose_name="Nome do Aluno")
    genero = models.CharField(max_length=2, choices=SEXO_CHOICES, blank=False, null=True, verbose_name="Sexo")
    data_da_avaliacao = models.DateField(auto_now_add=True, blank=False, null=False, verbose_name="Data da Avaliação")
    peso = models.DecimalField(max_digits=4, decimal_places=1, null=False, blank=False, verbose_name="Peso em Kg")
    altura = models.DecimalField(max_digits=3, decimal_places=0, null=False, blank=False, verbose_name="Altura em CM")
    IMC = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False, verbose_name="IMC (Índice de Massa corporal)")
    Gordura = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False, verbose_name="Percentual de Gordura")
    Massa_magra = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False, verbose_name="Percentual de Massa Magra")
    Profissao= models.CharField(max_length=36, null=True, blank=False, verbose_name="Profissão")
    Doencas_pre_existentes= models.TextField(max_length=512, null=False, blank=True, verbose_name="Doenças Pré Existentes")
    Laudos_e_Exames= models.FileField(upload_to='laudos_medicos', null=True, blank=True, verbose_name="Laudos e Exames Médicos")
    Habitos= models.TextField(max_length=1024, null=False, blank=False, verbose_name="Hábitos do Aluno")
    observacoes = models.TextField(max_length=140, null=True, blank=True, verbose_name="Observações")

    def __str__(self):

        return str(self.pk) + ' - ' + self.nome


class personal(models.Model):
    Nome = models.CharField(null=False, blank=False, max_length=64, verbose_name='Nome do Personal')
    Numero_CREF = models.CharField(null=False, blank=False, max_length=12, verbose_name='Número do CREF')
    TURNO_CHOICES = (
        ("1", "5:00 às 11:00"),
        ("2", "6:00 às 12:00"),
        ("3", "11:00 às 17:00"),
        ("4", "12:00 às 18:00"),
        ("5", "13:00 às 19:00"),
        ("6", "16:00 às 22:00")
    )
    Turno = models.CharField(choices=TURNO_CHOICES, max_length=4, blank=False, null=False, verbose_name='Turno de Serviço')
    SEV_CHOICES = (
        ("M", "Musculação"),
        ("F", "Fit Dance"),
        ("K", "Kangoo"),
        ("C", "Cross"),
        ("Fu", "Funcional"),
        ("P", "Pilates"),
        ("J", "Judô"),
        ("K", "Karatê")

    )
    Aula = models.CharField(choices=SEV_CHOICES, max_length=4, null=False, blank=False, verbose_name='Aula a Ministrar')
    observacoes = models.TextField(max_length=256, null=True, blank=True, verbose_name='Observações')

    def __str__(self):
        return str(self.Nome + ' - ' + self.Aula)



class ficha_de_saude(models.Model):
    VERDADEIRO_CHOICES = (
        ("S", "Sim"),
        ("N", "Não"),
        ("NI", "Não Informado")
    )
    personal = models.ForeignKey('personal', on_delete=models.DO_NOTHING, default=1, verbose_name='Personal Responsável')
    cliente = models.ForeignKey('avaliacao', on_delete=models.DO_NOTHING, default=1, verbose_name='Aluno')
    diabetes = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Diabetes")
    hipertensao = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Hipertensão")
    artrite = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Artrite")
    artrose = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Artrose")
    reumatismo = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Reumatismo")
    doencas_cardiacas = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Doenças Cardiacas")
    avc = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Já Sofreu AVC")
    fuma = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Tabagismo")
    BEBIDA_CHOICES = (
        ("1", "Sempre que Posso"),
        ("2", "Ocasionalmente"),
        ("3", "Raramente"),
        ("4", "Não Bebo")
    )
    bebe = models.CharField(max_length=1, choices=BEBIDA_CHOICES, blank=False, null=True, verbose_name="Bebe")
    observacoes = models.TextField(max_length=140, null=True, blank=True, verbose_name="Observações")

    def __str__(self):
        return str(self.cliente)




class treino(models.Model):

    personal = models.ForeignKey('personal', on_delete=models.DO_NOTHING, default=1, verbose_name='Personal Responsável')
    cliente = models.ForeignKey('avaliacao', on_delete=models.DO_NOTHING, default=1, verbose_name='Aluno')
    Treino_A = models.FileField(upload_to="Treino A", null=False, blank=False, verbose_name="Treino A")
    Treino_B = models.FileField(upload_to="Treino B", null=False, blank=False, verbose_name="Treino B")
    Treino_C = models.FileField(upload_to="Treino C", null=True, blank=True, verbose_name="Treino C")
    Treino_D = models.FileField(upload_to="Treino D", null=True, blank=True, verbose_name="Treino D")
    Treino_E = models.FileField(upload_to="Treino E", null=True, blank=True, verbose_name="Treino E")


    def __str__(self):
        return str(self.cliente + '-' + self.personal)


class objetivos(models.Model):
    VERDADEIRO_CHOICES = (
        ("S", "Sim"),
        ("N", "Não")
    )
    OBJ_CHOICES = (
        ("H", "Hipetrofia"),
        ("E", "Emagrecimanto"),
        ("C", "Condicionamento"),
        ("L", "Lazer")
    )
    Personal = models.ForeignKey('personal', on_delete=models.DO_NOTHING, default=1, verbose_name='Personal Responsável')
    cliente = models.ForeignKey('avaliacao', on_delete=models.DO_NOTHING, default=1, verbose_name='Aluno')
    obje = models.CharField(max_length=2, choices=OBJ_CHOICES, null=False, blank=False, verbose_name="Objetivo Principal")
    perda = models.CharField(max_length=1, choices=VERDADEIRO_CHOICES, null=False, blank=False, verbose_name="Perder Peso")
    Peso = models.DecimalField(max_digits=3, decimal_places=1, null=False, blank=False, verbose_name="Peso atual")
    Pesos = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, verbose_name="Quilos a Perder")
    Massa = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, verbose_name="Peso em Massa Magra a Ganhar")
    Pretencao = models.DecimalField(max_digits=1, decimal_places=0, null=False, blank=False, verbose_name="Frequencia de treino semanal (Dias)")
    observacoes = models.CharField(max_length=64, null=True, blank=False, verbose_name="Observações")

    def __str__(self):
        return str(self.cliente)


class medicamento(models.Model):
    TRUE_CHOICES = (
        ("S", "Sim"),
        ("N", "Não")
    )
    cliente = models.ForeignKey('avaliacao', on_delete=models.DO_NOTHING, default=1, verbose_name='Aluno')
    insulina=models.CharField(max_length=2, choices=TRUE_CHOICES, null=False, blank=False, verbose_name="Insulina")
    Antidepressivos=models.CharField(max_length=2, choices=TRUE_CHOICES, null=False, blank=False, verbose_name="Antidepressivos")
    Antihistaminicos=models.CharField(max_length=2, choices=TRUE_CHOICES, null=False, blank=False, verbose_name="Anti-Histaminicos (Alergia)")
    Betabloqueadores=models.CharField(max_length=2, choices=TRUE_CHOICES, null=False, blank=False, verbose_name="Betabloqueadores (Hipertensão)")
    Analgesicos=models.CharField(max_length=2, choices=TRUE_CHOICES, null=False, blank=False, verbose_name="Analgésicos")
    Ansiolitico=models.CharField(max_length=2, choices=TRUE_CHOICES, null=False, blank=False, verbose_name="Ansiolítico (Ansiedade)")
    suplementos_vit=models.CharField(max_length=2, choices=TRUE_CHOICES, null=False, blank=False, verbose_name="Suplementos Vitamínicos")
    observacoes = models.TextField(max_length=140, null=True, blank=True, verbose_name="Observações")

    def __str__(self):
        return str(self.cliente)


class nutricao(models.Model):
    Personal = models.ForeignKey('personal', on_delete=models.DO_NOTHING, default=1, verbose_name='Personal Responsável')
    cliente = models.ForeignKey('avaliacao', on_delete=models.DO_NOTHING, default=1, verbose_name='Aluno')
    Cafe=models.FileField(upload_to="Cafe_da_manha", null=False, blank=False, verbose_name="Café da manhã")
    lanche1=models.FileField(upload_to="Lanche_manhã", null=False, blank=False, verbose_name="Lanche da Manhã")
    Almoco=models.FileField(upload_to="Almoco", null=False, blank=False, verbose_name="Almoço")
    lanche2=models.FileField(upload_to="Lanche_tarde", null=False, blank=False, verbose_name="Lanche da Tarde")
    jantar=models.FileField(upload_to="Jantar", null=False, blank=False, verbose_name="Jantar")
    ceia=models.FileField(upload_to="Ceia_PT", null=False, blank=False, verbose_name="Ceia ou Pós Treino")
    observacoes = models.TextField(max_length=140, null=True, blank=True, verbose_name="Observações")

    def __str__(self):
        return str(self.pk + ' - ' + self.cliente)

