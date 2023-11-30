from django.shortcuts import redirect, render, HttpResponseRedirect
from django.urls import reverse
from .forms import LivroForm
from .models import LivroModel
from django.shortcuts import get_object_or_404

def index(request):
    if request.method == 'GET':
        return render(request, "index.html")
    else:
        return HttpResponseRedirect(reverse('core:index'))

def cadastro(request):
    if request.method == 'POST':
        form_livro = LivroForm(request.POST)
        if form_livro.is_valid():
            eleitor = LivroModel.objects.create(**form_livro.cleaned_data)
            return HttpResponseRedirect(reverse('core:index'))  
        else:
            contexto = {'formulario_livro': form_livro}
            return render(request, "cadastro.html", contexto)
    else:
        contexto = {'formulario_livro': LivroForm()}
        return render(request, 'cadastro.html', contexto)

def listar(request):
    if request.method == 'POST':
        livro_id = request.POST.get('livro_id', '')
        try:
            livro = LivroModel.objects.get(pk=livro_id)
            contexto = {'livro': livro}
        except ValueError:
            contexto = {}
        return render(request, "detalhes.html", contexto)
    else:
        livros = LivroModel.objects.all()
        contexto = {'livros': livros}
        return render(request, 'listar.html', contexto)

def deletar(request):
    if request.method == 'POST':
        livro_id = request.POST.get('livro_id')
        livro = LivroModel.objects.get(pk=livro_id)
        livro.delete()
        return render(request, 'index.html')

def atualizar(request):
    if request.method == 'POST':
        livro_id = request.POST.get('livro_id')
        livro = LivroModel.objects.get(pk=livro_id)
        form_livro = LivroForm(request.POST, instance=livro)
        if form_livro.is_valid():
            form_livro.save()
            return HttpResponseRedirect(reverse('core:index'))
        else:
            contexto = {'formulario_livro': form_livro}
            return render(request, "atualizar.html", contexto)      
    else: 
        contexto = {'formulario_livro': LivroForm()}
        return render(request, 'atualizar.html', contexto)