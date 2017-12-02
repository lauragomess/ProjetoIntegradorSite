from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from .models import Aluno,Tcc
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'core/home.html')
	
def tcc_detalhe(request):
		#tcc = get_object_or_404(Tcc, pk=pk)
		#tccs =Tcc.objects.filter(tcc__user__id=request.user.id).filter(tcc__pk=pk)
		tccs = Tcc.objects.all()
		return render(request, 'core/tcc_detalhe.html',{'tccs':tccs})
		

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Alunos').count() == 0, login_url='/')
def tccs(request):
	tccs = Tcc.objects.filter(tccs = request.user.id)
	return render(request, 'core/tccs.html',{'tcc':tcc})

#@login_required
#@user_passes_test(lambda u: u.groups.filter(name='Alunos').count() == 0, login_url='/')
#def tcc_detalhe(request, pk):
#    tcc = get_object_or_404(Tcc, pk=pk)
#    tccs =Tcc.objects.filter(tcc__user__id=request.user.id).filter(tcc__pk=pk)
#    return render(request, 'core/tcc_detalhe.html', {'tcc': tcc,
#    	'nome':nome,
#    	'aluno':aluno,
#    	'curso' : curso,
#    	
#    	})
