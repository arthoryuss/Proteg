from __future__ import unicode_literals
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User, UserAdmin)