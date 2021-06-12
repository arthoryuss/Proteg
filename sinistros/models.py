from django.db import models
from django.core import validators
from .choices import *
from django.conf import settings	
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
    UserManager)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from core.models import User

class Violacao (models.Model):

	conta = models.CharField ('Conta', max_length = 5)
	cliente = models.CharField ('Cliente', max_length = 30)
	bi = models.FileField(upload_to="uploads/%Y/%m/%d",null=True, blank=True)
	bo = models.FileField('Relatório do Sistema', upload_to="uploads/%Y/%m/%d",null=True, blank=True)
	nome_contato = models.CharField ('Contato Feedback', max_length = 40)
	procedimento = models.CharField(
			'Procedimento foi cumprido?',
			max_length=25,
			choices=YESORNOT_MODELS ,
		)
	tecnica = models.CharField(
			'Sistema funcionou?',
			max_length=25,
			choices=YESORNOT_MODELS ,
		)
	ressarcimento = models.IntegerField ('Ressarcimento',null=True)
	horario_inicio = models.TimeField('Horário Início', auto_now_add=False,null=True, blank=True)
	horario_fim = models.TimeField('Horário Fim', auto_now_add=False,null=True, blank=True)
	data = models.DateField ('Data da Violação')
	cidade =  models.CharField ('Cidade', max_length = 30)
	bairro =  models.CharField ('Bairro', max_length = 30)
	tratativa = models.CharField(
			'A tratativa foi finalizada?',
			max_length=25,
			choices=YESORNOT_MODELS ,
			)
	class Meta:
		verbose_name = 'Violação'
		verbose_name_plural = 'Violações'

class Arquivo(models.Model):
    arquivo = models.FileField(upload_to="uploads/%Y/%m/%d")
    violacao = models.ForeignKey(Violacao, on_delete=models.CASCADE, related_name='arquivos')
    class Meta:
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'

class Comentarios(models.Model):
	user = models.ForeignKey(User, related_name='comentarios', on_delete=models.CASCADE)
	comentario = models.TextField ('Descrição')
	violacao = models.ForeignKey(Violacao, on_delete=models.CASCADE, related_name='comentarios')
	data = models.DateTimeField(auto_now_add=True, blank=True)
	class Meta:
		verbose_name = 'Comentário'
		verbose_name_plural = 'Comentários'

