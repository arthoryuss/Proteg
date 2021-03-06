# Generated by Django 3.2.4 on 2021-06-11 23:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Violacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conta', models.CharField(max_length=5, verbose_name='Conta')),
                ('cliente', models.CharField(max_length=30, null=True, verbose_name='Cliente')),
                ('bi', models.FileField(null=True, upload_to='uploads/%Y/%m/%d')),
                ('bo', models.FileField(null=True, upload_to='uploads/%Y/%m/%d', verbose_name='Relatório do Sistema')),
                ('nome_contato', models.CharField(max_length=40, verbose_name='Contato Feedback')),
                ('procedimento', models.CharField(choices=[('', ''), ('sim', 'Sim'), ('nao', 'Não')], max_length=25, verbose_name='Procedimento foi cumprido?')),
                ('tecnica', models.CharField(choices=[('', ''), ('sim', 'Sim'), ('nao', 'Não')], max_length=25, verbose_name='Sistema funcionou?')),
                ('ressarcimento', models.IntegerField(null=True, verbose_name='Ressarcimento')),
                ('horario_inicio', models.TimeField(null=True, verbose_name='Horário Início')),
                ('horario_fim', models.TimeField(null=True, verbose_name='Horário Fim')),
                ('data', models.DateField(verbose_name='Data da Violação')),
                ('cidade', models.CharField(max_length=30, verbose_name='Cidade')),
                ('bairro', models.CharField(max_length=30, verbose_name='Bairro')),
                ('tratativa', models.CharField(choices=[('', ''), ('sim', 'Sim'), ('nao', 'Não')], max_length=25, verbose_name='A tratativa foi finalizada?')),
            ],
            options={
                'verbose_name': 'Violação',
                'verbose_name_plural': 'Violações',
            },
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(verbose_name='Descrição')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to=settings.AUTH_USER_MODEL)),
                ('violacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='sinistros.violacao')),
            ],
            options={
                'verbose_name': 'Comentário',
                'verbose_name_plural': 'Comentários',
            },
        ),
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='uploads/%Y/%m/%d')),
                ('violacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arquivos', to='sinistros.violacao')),
            ],
            options={
                'verbose_name': 'Arquivo',
                'verbose_name_plural': 'Arquivos',
            },
        ),
    ]
