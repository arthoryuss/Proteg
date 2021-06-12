from django.contrib import admin
from .models import *

# Register your models here.

class InterfoneAdmin(admin.ModelAdmin):
	model = Interfone

admin.site.register(Interfone, InterfoneAdmin)