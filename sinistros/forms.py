from django.forms import *
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

class ComentariosForm(ModelForm):

	comentario = CharField(widget=forms.Textarea, label ='Comentário', required = True)

	class Meta:
		model = Comentarios
		fields = ['comentario']
		
