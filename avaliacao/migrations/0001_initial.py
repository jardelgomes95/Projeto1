# Generated by Django 3.1.7 on 2021-05-26 11:22
# Generated by Django 3.1.7 on 2021-05-23 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64, verbose_name='Nome do Aluno')),
                ('genero', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('N', 'Não Quero Informar')], max_length=2, null=True, verbose_name='Sexo')),
                ('data_da_avaliacao', models.DateField(auto_now_add=True, verbose_name='Data da Avaliação')),
                ('peso', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Peso em Kg')),
                ('altura', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Altura em CM')),
                ('IMC', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='IMC (Índice de Massa corporal)')),
                ('Gordura', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Percentual de Gordura')),
                ('Massa_magra', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Percentual de Massa Magra')),
                ('Profissao', models.CharField(max_length=36, null=True, verbose_name='Profissão')),
                ('Doencas_pre_existentes', models.TextField(blank=True, max_length=512, verbose_name='Doenças Pré Existentes')),
                ('Laudos_e_Exames', models.FileField(blank=True, null=True, upload_to='laudos_medicos', verbose_name='Laudos e Exames Médicos')),
                ('Habitos', models.TextField(max_length=1024, verbose_name='Hábitos do Aluno')),
                ('observacoes', models.TextField(blank=True, max_length=140, null=True, verbose_name='Observações')),
            ],
        ),
        migrations.CreateModel(
            name='personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=64, verbose_name='Nome do Personal')),
                ('Numero_CREF', models.CharField(max_length=12, verbose_name='Número do CREF')),
                ('Turno', models.CharField(choices=[('1', '5:00 às 11:00'), ('2', '6:00 às 12:00'), ('3', '11:00 às 17:00'), ('4', '12:00 às 18:00'), ('5', '13:00 às 19:00'), ('6', '16:00 às 22:00')], max_length=4, verbose_name='Turno de Serviço')),
                ('Aula', models.CharField(choices=[('M', 'Musculação'), ('F', 'Fit Dance'), ('K', 'Kangoo'), ('C', 'Cross'), ('Fu', 'Funcional'), ('P', 'Pilates'), ('J', 'Judô'), ('K', 'Karatê')], max_length=4, verbose_name='Aula a Ministrar')),
                ('observacoes', models.TextField(blank=True, max_length=256, null=True, verbose_name='Observações')),
            ],
        ),
        migrations.CreateModel(
            name='treino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Treino_A', models.FileField(upload_to='Treino A', verbose_name='Treino A')),
                ('Treino_B', models.FileField(upload_to='Treino B', verbose_name='Treino B')),
                ('Treino_C', models.FileField(blank=True, null=True, upload_to='Treino C', verbose_name='Treino C')),
                ('Treino_D', models.FileField(blank=True, null=True, upload_to='Treino D', verbose_name='Treino D')),
                ('Treino_E', models.FileField(blank=True, null=True, upload_to='Treino E', verbose_name='Treino E')),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='avaliacao.avaliacao', verbose_name='Aluno')),
                ('personal', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='avaliacao.personal', verbose_name='Personal Responsável')),
            ],
        ),
        migrations.CreateModel(
            name='objetivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obje', models.CharField(choices=[('H', 'Hipetrofia'), ('E', 'Emagrecimanto'), ('C', 'Condicionamento'), ('L', 'Lazer')], max_length=2, verbose_name='Objetivo Principal')),
                ('perda', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Perder Peso')),
                ('Peso', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Peso atual')),
                ('Pesos', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Quilos a Perder')),
                ('Massa', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Peso em Massa Magra a Ganhar')),
                ('Pretencao', models.DecimalField(decimal_places=0, max_digits=1, verbose_name='Frequencia de treino semanal (Dias)')),
                ('observacoes', models.CharField(max_length=64, null=True, verbose_name='Observações')),
                ('Personal', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='avaliacao.personal', verbose_name='Personal Responsável')),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='avaliacao.avaliacao', verbose_name='Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='nutricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cafe', models.FileField(upload_to='Cafe_da_manha', verbose_name='Café da manhã')),
                ('lanche1', models.FileField(upload_to='Lanche_manhã', verbose_name='Lanche da Manhã')),
                ('Almoco', models.FileField(upload_to='Almoco', verbose_name='Almoço')),
                ('lanche2', models.FileField(upload_to='Lanche_tarde', verbose_name='Lanche da Tarde')),
                ('jantar', models.FileField(upload_to='Jantar', verbose_name='Jantar')),
                ('ceia', models.FileField(upload_to='Ceia_PT', verbose_name='Ceia ou Pós Treino')),
                ('observacoes', models.TextField(blank=True, max_length=140, null=True, verbose_name='Observações')),
                ('Personal', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='avaliacao.personal', verbose_name='Personal Responsável')),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='avaliacao.avaliacao', verbose_name='Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insulina', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=2, verbose_name='Insulina')),
                ('Antidepressivos', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=2, verbose_name='Antidepressivos')),
                ('Antihistaminicos', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=2, verbose_name='Anti-Histaminicos (Alergia)')),
                ('Betabloqueadores', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=2, verbose_name='Betabloqueadores (Hipertensão)')),
                ('Analgesicos', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=2, verbose_name='Analgésicos')),
                ('Ansiolitico', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=2, verbose_name='Ansiolítico (Ansiedade)')),
                ('suplementos_vit', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=2, verbose_name='Suplementos Vitamínicos')),
                ('observacoes', models.TextField(blank=True, max_length=140, null=True, verbose_name='Observações')),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='avaliacao.avaliacao', verbose_name='Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='ficha_de_saude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diabetes', models.CharField(choices=[('S', 'Sim'), ('N', 'Não'), ('NI', 'Não Informado')], max_length=2, null=True, verbose_name='Diabetes')),
                ('hipertensao', models.CharField(choices=[('S', 'Sim'), ('N', 'Não'), ('NI', 'Não Informado')], max_length=2, null=True, verbose_name='Hipertensão')),
                ('artrite', models.CharField(choices=[('S', 'Sim'), ('N', 'Não'), ('NI', 'Não Informado')], max_length=2, null=True, verbose_name='Artrite')),
                ('artrose', models.CharField(choices=[('S', 'Sim'), ('N', 'Não'), ('NI', 'Não Informado')], max_length=2, null=True, verbose_name='Artrose')),
                ('reumatismo', models.CharField(choices=[('S', 'Sim'), ('N', 'Não'), ('NI', 'Não Informado')], max_length=2, null=True, verbose_name='Reumatismo')),
                ('doencas_cardiacas', models.CharField(choices=[('S', 'Sim'), ('N', 'Não'), ('NI', 'Não Informado')], max_length=2, null=True, verbose_name='Doenças Cardiacas')),
                ('avc', models.CharField(choices=[('S', 'Sim'), ('N', 'Não'), ('NI', 'Não Informado')], max_length=2, null=True, verbose_name='Já Sofreu AVC')),
                ('fuma', models.CharField(choices=[('S', 'Sim'), ('N', 'Não'), ('NI', 'Não Informado')], max_length=2, null=True, verbose_name='Tabagismo')),
                ('bebe', models.CharField(choices=[('1', 'Sempre que Posso'), ('2', 'Ocasionalmente'), ('3', 'Raramente'), ('4', 'Não Bebo')], max_length=1, null=True, verbose_name='Bebe')),
                ('observacoes', models.TextField(blank=True, max_length=140, null=True, verbose_name='Observações')),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='avaliacao.avaliacao', verbose_name='Aluno')),
                ('personal', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='avaliacao.personal', verbose_name='Personal Responsável')),
            ],
        ),
    ]
