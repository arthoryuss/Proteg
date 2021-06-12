from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='sinistros'

urlpatterns = [ 
	path("", views.violacoes, name='violacoes'),
	path("detalhes/<id>", views.detalhes, name='detalhes'),
] 

