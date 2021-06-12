from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from django.conf import settings

# Create your views here.
User = get_user_model()


@login_required
def violacoes(request):
	info = Violacao.objects.order_by('-id').all()
	context = {
		'info' : info,
		}
	return render(request, 'violacoes.html', context)

@login_required
def detalhes(request, id):
	template_name = 'detalhes_violacao.html'
	detail = Violacao.objects.get(id=id)
	#teste = detail.horario_fim - detail.horario_inicio
	detail2 = Comentarios.objects.filter(violacao_id = id)
	form = ComentariosForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			temp = form.save(commit=False)
			temp.violacao_id = id
			temp.user_id = request.user.id
			temp.save()
			messages.success(
                request, 'Comentário adicionado com sucesso'
            ) 

	
	context = {
            'detail':detail,
            'form': form,
            'detail2':detail2,
        }
	return render(request, template_name, context)
