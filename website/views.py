from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProyectoForm, RegistroForm
from .models import Proyecto
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
        return render(request, 'crear_proyecto.html', {'form': form})

@login_required
def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk = pk)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'crear_proyecto.html', { 'form': form })

@login_required
def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk = pk)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('lista_proyectos')
    return render(request, 'eliminar_proyecto.html', { 'proyecto': proyecto })

@login_required
def lista_proyectos(request):
    proyectos = Proyecto.objects.all() # SELECT * FROM proyecto
    return render(request, 'lista_proyectos.html', { 'proyectos': proyectos })

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Bienvenido, {user.username}.')
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})
