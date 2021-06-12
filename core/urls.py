from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='core'

urlpatterns = [ 
	path("", views.base, name='base'),
	path('login/', LoginView.as_view(template_name = 'login.html'), 
    	 name='login'),
    path('logout/', LogoutView.as_view(next_page= 'violacao:login'), 
    	 name='logout'),
] 
