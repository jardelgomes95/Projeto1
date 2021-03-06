# Generated by Django 3.1.7 on 2021-05-27 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='matricula',
            fields=[
                ('Nome', models.CharField(max_length=40, verbose_name='Nome do Cliente')),
                ('CPF', models.CharField(max_length=11, null=True, verbose_name='CPF')),
                ('email', models.EmailField(max_length=40, verbose_name='Email')),
                ('telefone', models.CharField(max_length=9, null=True, verbose_name='Telefone')),
                ('Data_da_matricula', models.DateField(auto_now_add=True, verbose_name='Data da Matricula')),
                ('Plano', models.CharField(choices=[('1', 'Musculação'), ('2', 'Musculação + Cross'), ('3', 'Musculação + Cross + Fit Dance'), ('4', 'Personalizado')], max_length=1, verbose_name='Plano')),
                ('Numero_matricula', models.AutoField(primary_key=True, serialize=False, verbose_name='Número da Matricula')),
                ('Foto_aluno', models.ImageField(upload_to='alunos', verbose_name='Foto do Aluno')),
                ('Hora_treino', models.TimeField(blank=True, verbose_name='Horário de Treino')),
                ('observacoes', models.TextField(blank=True, max_length=1024, verbose_name='Observações')),
            ],
        ),
        migrations.CreateModel(
            name='pilates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], max_length=1, verbose_name='Turno')),
                ('Hora', models.TimeField(verbose_name='Hora')),
                ('Lesoes', models.CharField(blank=True, choices=[('S', 'Sim'), ('N', 'Não'), ('O', 'Não Sei'), ('X', 'Não Diagnosticado')], max_length=2, null=True, verbose_name='Dores ou Lesões')),
                ('Idade', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True, verbose_name='Idade')),
                ('plano', models.CharField(blank=True, choices=[('L', 'La Carte'), ('M', 'Musculação + Pilates'), ('O', 'Outro')], max_length=2, verbose_name='Plano')),
                ('Observacao', models.TextField(blank=True, max_length=64, null=True, verbose_name='Observações')),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='vendas.matricula', verbose_name='Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='outros_servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pilates', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Pilates')),
                ('muay_thai', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Muay Thai')),
                ('Aerobox', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Aerobox')),
                ('Treino_Funcional', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Treino Funcional')),
                ('Kangoo_Jump', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Kangoo Jump')),
                ('Obeservacoes', models.TextField(blank=True, max_length=256, null=True, verbose_name='Observações')),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='vendas.matricula', verbose_name='Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='muaythai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Turno', models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], max_length=1, verbose_name='Turno')),
                ('Hora', models.TimeField(verbose_name='Hora')),
                ('Observacao', models.TextField(blank=True, max_length=64, null=True, verbose_name='Observações')),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='vendas.matricula', verbose_name='Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='kangoodance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Turno', models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], max_length=1, verbose_name='Turno')),
                ('Hora', models.TimeField(verbose_name='Hora')),
                ('Observacao', models.TextField(blank=True, max_length=64, null=True, verbose_name='Observações')),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='vendas.matricula', verbose_name='Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='funcional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Turno', models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], max_length=1, verbose_name='Turno')),
                ('Hora', models.TimeField(verbose_name='Hora')),
                ('Observacao', models.TextField(blank=True, max_length=64, null=True, verbose_name='Observações')),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='vendas.matricula', verbose_name='Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='frequencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aula', models.CharField(choices=[('M', 'Musculação'), ('F', 'Fit Dance'), ('K', 'Kangoo'), ('C', 'Cross'), ('Fu', 'Funcional'), ('P', 'Pilates'), ('J', 'Judô'), ('K', 'Karatê')], max_length=2, verbose_name='Serviço')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Data')),
                ('nome', models.CharField(max_length=48, verbose_name='Nome do Aluno')),
                ('hora1', models.TimeField(verbose_name='Hora de Entrada')),
                ('hora2', models.TimeField(null=True, verbose_name='Hora de Saída')),
                ('Observacao', models.TextField(blank=True, max_length=256, null=True, verbose_name='Observações')),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='vendas.matricula', verbose_name='Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='fitdance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turn', models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], max_length=1, verbose_name='Turno')),
                ('Hora', models.TimeField(verbose_name='Hora')),
                ('Observacao', models.TextField(blank=True, max_length=64, null=True, verbose_name='Observações')),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='vendas.matricula', verbose_name='Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='financeiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plano_de_Pagamento', models.CharField(choices=[('M', 'Mensal'), ('S', 'Semestral'), ('T', 'Trimestral'), ('A', 'Anual')], max_length=1, verbose_name='Plano de Pagamento')),
                ('Data_de_vencimento', models.IntegerField(default=15, verbose_name='Dia de Vencimento')),
                ('Valor', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor')),
                ('Forma_de_Pagamento', models.CharField(choices=[('B', 'Boleto'), ('C', 'Cartão de Crédito'), ('P', 'Pix'), ('T', 'TED/Débito')], max_length=1, verbose_name='Forma de Pagamento')),
                ('observacoes', models.TextField(blank=True, max_length=1024, verbose_name='Observações')),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='vendas.matricula', verbose_name='Aluno')),
            ],
        ),
    ]
