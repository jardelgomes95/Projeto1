from django.db import models
# Create your models here.

class matricula(models.Model):
        PLANO_CHOICES = (
                ("1", "Musculação"),
                ("2", "Musculação + Cross"),
                ("3", "Musculação + Cross + Fit Dance"),
                ("4", "Personalizado")
        )
        Nome= models.CharField(max_length=40, blank=False, verbose_name="Nome do Cliente")
        CPF= models.CharField(max_length=11, null=True, blank=False, verbose_name="CPF")
        email= models.EmailField(max_length=40, blank=False, verbose_name="Email")
        telefone= models.CharField(max_length=9, blank=False, null=True, verbose_name="Telefone")
        Data_da_matricula= models.DateField(auto_now_add=True, null=False, blank=False, verbose_name="Data da Matricula")
        Plano= models.CharField(max_length=1, null=False, blank=False, choices=PLANO_CHOICES, verbose_name="Plano")
        Numero_matricula= models.AutoField(primary_key=True, blank=False, null=False, verbose_name="Número da Matricula")
        Foto_aluno= models.ImageField(blank=False, null=False, verbose_name="Foto do Aluno", upload_to='alunos')
        Hora_treino= models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=False, verbose_name="Horário de Treino")
        observacoes= models.TextField(max_length=1024, blank=True, null=False, verbose_name="Observações")

        def __str__(self):
                return str(self.pk) + ' - ' + self.Nome + ' - ' + self.CPF

class outros_servico(models.Model):
        SN_CHOICES = (
                ("S", "Sim"),
                ("N", "Não")
        )
        cliente = models.ForeignKey('matricula', on_delete=models.DO_NOTHING, default=1, verbose_name='Aluno')
        Pilates= models.CharField(choices=SN_CHOICES, max_length=1, null=False, blank=False, verbose_name="Pilates")
        muay_thai= models.CharField(choices=SN_CHOICES, max_length=1, null=False, blank=False, verbose_name="Muay Thai")
        Aerobox= models.CharField(choices=SN_CHOICES, max_length=1, null=False, blank=False, verbose_name="Aerobox")
        Treino_Funcional= models.CharField(choices=SN_CHOICES, max_length=1, null=False, blank=False, verbose_name="Treino Funcional")
        Kangoo_Jump= models.CharField(choices=SN_CHOICES, max_length=1, null=False, blank=False, verbose_name="Kangoo Jump")
        Obeservacoes= models.TextField(max_length=256, null=True, blank=True, verbose_name="Observações")

        def __str__(self):
                return str(self.pk)

class financeiro(models.Model):
        PLAN_CHOICES = (
                ("M", "Mensal"),
                ("S", "Semestral"),
                ("T", "Trimestral"),
                ("A", "Anual")
        )
        cliente = models.ForeignKey('matricula', on_delete=models.DO_NOTHING, default=1, verbose_name='Aluno')
        Plano_de_Pagamento= models.CharField(max_length=1, null=False, blank=False, choices=PLAN_CHOICES, verbose_name="Plano de Pagamento")
        Data_de_vencimento= models.IntegerField(default=15, blank=False, null=False, verbose_name="Dia de Vencimento")
        Valor = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, verbose_name="Valor")
        VALOR_CHOICES = (
                ("B", "Boleto"),
                ("C", "Cartão de Crédito"),
                ("P", "Pix"),
                ("T", "TED/Débito")
        )
        Forma_de_Pagamento= models.CharField(max_length=1, null=False, blank=False, choices=VALOR_CHOICES, verbose_name="Forma de Pagamento")
        observacoes = models.TextField(max_length=1024, blank=True, null=False, verbose_name="Observações")

        def __str__(self):
                return str(self.pk) + ' - ' + self.observacoes

class pilates(models.Model):
        TURNO_CHOICES = (
                ("M", "Manhã"),
                ("T", "Tarde"),
                ("N", "Noite")
        )
        cliente = models.ForeignKey('matricula', on_delete=models.DO_NOTHING, default=1, verbose_name='Aluno')
        turno = models.CharField(max_length=1, choices=TURNO_CHOICES, blank=False, null=False, verbose_name="Turno")
        Hora = models.TimeField(auto_now_add=False, null=False, blank=False, verbose_name="Hora")
        LESAO_CHOICES = (
                ("S", "Sim"),
                ("N", "Não"),
                ("O", "Não Sei"),
                ("X", "Não Diagnosticado")
        )
        Lesoes = models.CharField(max_length=2, choices=LESAO_CHOICES, null=True, blank=True, verbose_name="Dores ou Lesões")
        Idade = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank=True, verbose_name="Idade")
        PLAN_CHOICES = (
                ("L", "La Carte"),
                ("M", "Musculação + Pilates"),
                ("O", "Outro")
        )
        plano = models.CharField(max_length=2, choices=PLAN_CHOICES, blank=True, null=False, verbose_name="Plano")
        Observacao = models.TextField(max_length=64, null=True, blank=True, verbose_name="Observações")

        def __str__(self):
                return str(self.pk) + ' - ' + self.Observacao

class fitdance(models.Model):
        TURN_CHOICES = (
        ("M", "Manhã"),
        ("T", "Tarde"),
        ("N", "Noite")
        )
        cliente = models.ForeignKey('matricula', on_delete=models.DO_NOTHING, default=1, verbose_name='Aluno')
        turn = models.CharField(max_length=1, choices=TURN_CHOICES, blank=False, null=False, verbose_name="Turno")
        Hora = models.TimeField(auto_now_add=False, null=False, blank=False, verbose_name="Hora")
        Observacao = models.TextField(max_length=64, null=True, blank=True, verbose_name="Observações")

        def __str__(self):
                return str(self.pk) + ' - ' + self.Observacao

class kangoodance(models.Model):
        TUR_CHOICES = (
        ("M", "Manhã"),
        ("T", "Tarde"),
        ("N", "Noite")
        )
        cliente = models.ForeignKey('matricula', on_delete=models.DO_NOTHING, default=1, verbose_name='Aluno')
        Turno = models.CharField(max_length=1, choices=TUR_CHOICES, blank=False, null=False, verbose_name="Turno")
        Hora = models.TimeField(auto_now_add=False, null=False, blank=False, verbose_name="Hora")
        Observacao = models.TextField(max_length=64, null=True, blank=True, verbose_name="Observações")

        def __str__(self):
                return str(self.pk) + ' - ' + self.Observacao

class funcional(models.Model):
        TUNO_CHOICES = (
        ("M", "Manhã"),
        ("T", "Tarde"),
        ("N", "Noite")
)
        cliente = models.ForeignKey('matricula', on_delete=models.DO_NOTHING, default=1, verbose_name='Aluno')
        Turno = models.CharField(max_length=1, choices=TUNO_CHOICES, blank=False, null=False, verbose_name="Turno")
        Hora = models.TimeField(auto_now_add=False, null=False, blank=False, verbose_name="Hora")
        Observacao = models.TextField(max_length=64, null=True, blank=True, verbose_name="Observações")

        def __str__(self):
                return str(self.pk) + ' - ' + self.Observacao

class muaythai(models.Model):
        TUO_CHOICES = (
        ("M", "Manhã"),
        ("T", "Tarde"),
        ("N", "Noite")
)
        cliente = models.ForeignKey('matricula', on_delete=models.DO_NOTHING, default=1, verbose_name='Aluno')
        Turno = models.CharField(max_length=1, choices=TUO_CHOICES, blank=False, null=False, verbose_name="Turno")
        Hora = models.TimeField(auto_now_add=False, null=False, blank=False, verbose_name="Hora")
        Observacao = models.TextField(max_length=64, null=True, blank=True, verbose_name="Observações")

class frequencia(models.Model):
        SE_CHOICES = (
                ("M", "Musculação"),
                ("F", "Fit Dance"),
                ("K", "Kangoo"),
                ("C", "Cross"),
                ("Fu", "Funcional"),
                ("P", "Pilates"),
                ("J", "Judô"),
                ("K", "Karatê")

        )
        cliente = models.ForeignKey('matricula', on_delete=models.DO_NOTHING, default=1, verbose_name='Aluno')
        aula= models.CharField(max_length=2, choices=SE_CHOICES, verbose_name="Serviço", null=False, blank=False)
        data= models.DateField(auto_now_add=True, verbose_name="Data", null=False, blank=False)
        nome= models.CharField(max_length=48, verbose_name="Nome do Aluno", null=False, blank=False)
        hora1= models.TimeField(auto_now_add=False, verbose_name="Hora de Entrada", blank=False, null=False)
        hora2= models.TimeField(auto_now_add=False, verbose_name="Hora de Saída", blank=False, null=True)
        Observacao= models.TextField(max_length=256, verbose_name="Observações", blank=True, null=True)

        def __str__(self):
                return str(self.pk) + ' - ' + self.Observacao