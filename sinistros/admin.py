from __future__ import unicode_literals
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import *

# Register your models here.

class ArquivoInline(admin.StackedInline):
	model = Arquivo
class ComentariosInline(admin.StackedInline):
	model = Comentarios
class ViolacaoAdmin(admin.ModelAdmin):
	inlines = (ComentariosInline, ArquivoInline,)
	list_display = ('conta', 'cidade', 'bairro', 'data', 'tratativa')

admin.site.register(Violacao, ViolacaoAdmin)
