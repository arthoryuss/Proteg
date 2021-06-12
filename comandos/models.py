from django.db import models
from .choices import *

# Create your models here.
class Interfone (models.Model):

	
	modelo = models.CharField(
			'Modelo',
			max_length=25,
			choices=INTER_MODELS ,
		)
	ip = models.CharField ('IP', max_length = 50)
	porta = models.CharField ('Porta', max_length = 6)
	login = models.CharField ('Login', max_length = 25)
	senha = models.CharField ('Senha', max_length = 25)
	status = models.BooleanField ('Ativo', default=True)


	def __str__(self):
		return self.ip



#class Alarm (models.Model):

#	sensor_alarm = models.OneToOneField(Sensor, related_name='sensor_alarm', on_delete=models.CASCADE) 
#	tipo = models.CharField(
#			'Critério',
#			max_length=25,
#			choices=ALARMTYPE_CHOICES,
#		)
#	limit = models.FloatField ('Valor Limite')
#	date_finish = models.DateField ('Data para término do alarme')
#	status= models.BooleanField ('Repetir', default=False)
#	send_email= models.BooleanField ('Email enviado', default=False)
#	datecreation = models.DateTimeField('Data da Criação', auto_now_add=True)