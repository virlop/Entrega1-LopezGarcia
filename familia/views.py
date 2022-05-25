from urllib import request
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render
from familia.forms import PersonaForm, BuscarPersonasForm, PerroForm, GatoForm
from familia.models import Persona, Mascota, Gato, Perro

def index(request):
    personas = Persona.objects.all()
    gatos = Gato.objects.all()
    perros = Perro.objects.all()
    template = loader.get_template('familia/lista_familiares.html')
    context = {
        'personas': personas,
        'gatos' : gatos,
        'perros' : perros
    }
    return HttpResponse(template.render(context, request))



def agregar_familiar(request):

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            altura = form.cleaned_data['altura']
            Persona(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento, altura=altura).save()

            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'familia/form_carga.html', {'form': form})

def agregar_mascota_gato(request):
    if request.method == "POST":
        form = GatoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            fecha_adopcion = form.cleaned_data['fecha_adopcion'] 
            color_pelaje = form.cleaned_data['color_pelaje']
            Gato(nombre = nombre, fecha_adopcion = fecha_adopcion, color_pelaje = color_pelaje).save()
            return HttpResponseRedirect("/")
        
    elif request.method == "GET":
        form = GatoForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")
    return render(request, 'familia/form_carga_gato.html', {'form': form})

def agregar_mascota_perro(request):
    if request.method == "POST":
        form = PerroForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            fecha_adopcion = form.cleaned_data['fecha_adopcion'] 
            raza = form.cleaned_data['raza']
            Perro(nombre = nombre, fecha_adopcion = fecha_adopcion, raza = raza).save()
            return HttpResponseRedirect("/")
        
    elif request.method == "GET":
        form = PerroForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")
    return render(request, 'familia/form_carga_perro.html', {'form': form})

def borrar(request, identificador):
    if request.method == "GET":
        persona = Persona.objects.filter(id=int(identificador)).first()
        if persona:
            persona.delete()
        return HttpResponseRedirect("/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar(request, identificador):
    pass


def buscar(request):
    if request.method == "GET":
        form_busqueda = BuscarPersonasForm()
        return render(request, 'familia/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarPersonasForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            personas = Persona.objects.filter(nombre__icontains=palabra_a_buscar)

        return  render(request, 'familia/lista_familiares.html', {"personas": personas})
    