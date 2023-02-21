from django.shortcuts import render
from django.http import HttpResponse
from App1.models import *
from App1.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

#------------------------------------------

def inicioSesion(request):
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get ("username")
                  contra = form.cleaned_data.get ("password")

                  user = authenticate(username = usuario, password = contra)

                  if user:
                        login (request, user)

                        return render (request, "App1/inicio.html", {"mensaje":f"BIENVENIDO {user}"})

            else:
                  return render (request, "App1/inicio.html", {"mensaje":"DATOS INCORRECTOS"})

      else:
            form = AuthenticationForm()

      return render (request, "App1/login.html", {"formulario":form})

def registro(request):
      form_class = UsuarioRegistro
      form = form_class(request.POST or None) 
      if request.method == "POST":
            form = UsuarioRegistro(request.POST)

            if form.is_valid():
                  usernme= form.cleaned_data["username"]
                  form.save()
                  return render (request, "App1/inicio.html", {"mensaje":"USUARIO CREADO"})

      else:
            form = UsuarioRegistro()
      
      return render (request, "App1/registro.html", {"formulario":form})

def editarUsuario(request):
      usuario = request.user

      if request.method == "POST":
            form: FormularioEditar(request.POST)

            if form.is_valid():

                  info= form.cleaned_data
                  
                  usuario.email = info ["email"]
                  usuario.set_password(info["password1"])
                  usuario.first_name = info ["first_name"]
                  usuario.last_name = info ["last_name"]
                  usuario.save()

                  return render (request, "App1/inicio.html")

      else:
            form = FormularioEditar(initial={
                  "email":usuario.email, 
                  "fist_name":usuario.first_name,
                  "last_name":usuario.last_name,
                  })
      
      return render (request, "App1/editarPerfil.html", {"formulario":form,"usuario":usuario})

def inicio(request):
      return render(request, "App1/inicio.html")

def estudiante(request):

    todas= Estudiantes.objects.all()
    return  render (request, "App1/estudiantes.html")


 #Para Carreras.

def carrera(request):

    todas= Carreras.objects.all()
    return  render (request, "App1/carreras.html")

def carreraFormulario(request):

      if request.method == "POST":

            formulario1 = CarreraFormulario(request.POST)
            if formulario1.is_valid():
                  info = formulario1.cleaned_data
                  carrera = Carreras(nombre=info['nombre'],camada=info['camada'])
                  carrera.save()
                  return  render (request, "App1/inicio.html")

      else: 
            formulario1 = CarreraFormulario()

      return  render(request, "App1/carreraFormulario.html", {"form1":formulario1})

#Para Profesores.

def profesor(request):

    todas= Profesores.objects.all()
    return  render (request, "App1/profesores.html")

#Para buscar

def busquedaCamada (request):
      return  render (request, "App1/busquedaCamada.html")

def resultados (request):

      if  request.GET["camada"]:
            camada = request.GET['camada'] 
            carrera = Carreras.objects.filter(camada__icontains=camada)
            return render(request, "App1/resultados.html", {"nombre":carrera, "camada":camada})
      else: 
            respuesta = "No enviaste datos"


      return  HttpResponse(respuesta)

@login_required
def leerProfesores (request):
      profesores = Profesores.objects.all()
      contexto = {"teachers": profesores}
      return render (request, "App1/leerProfesores.html", contexto)

@login_required
def crearProfesores (request):
      if request.method == "POST":

            formulario2 = ProfesorFormulario(request.POST)
            if formulario2.is_valid():
                  info = formulario2.cleaned_data
                  profesor = Profesores(nombre=info['nombre'],carrera=info['carrera'])
                  profesor.save()
                  return  render (request, "App1/inicio.html")

      else: 
            formulario2 = ProfesorFormulario()

      return  render(request, "App1/profesorFormulario.html", {"form2":formulario2})

@login_required
def eliminarProfesores (request, profesorNombre):
      profesor = Profesores.objects.get(nombre=profesorNombre)
      profesor.delete()

      profesores= Profesores.objects.all()
      contexto= {"teachers": profesores}
      return render (request, "App1/leerProfesores.html", contexto)

@login_required
def editarProfesores (request, profesorNombre):
      profesor = Profesores.objects.get(nombre=profesorNombre)
      
      if request.method == "POST":
            formulario3 = ProfesorFormulario(request.POST)
            if formulario3.is_valid():
                  info = formulario3.cleaned_data
                  profesor.nombre = info ["nombre"]
                  profesor.carrera = info ["carrera"]
                  profesor.save()
                  return  render (request, "App1/inicio.html")

      else: 
            formulario3 = ProfesorFormulario(initial={"nombre":profesor.nombre, "carrera":profesor.carrera} )

      return  render(request, "App1/editarProfesores.html", {"form3":formulario3, "nombre":profesorNombre})

class ListaCarreras(LoginRequiredMixin,ListView):
      model = Carreras
      template_name = "/App1/carreras_list.html"

class DetalleCarreras(LoginRequiredMixin, DetailView):
      model = Carreras

class CrearCarreras(LoginRequiredMixin, CreateView):
      model = Carreras
      success_url = "/App1/carreras/"
      fields = ["nombre", "camada"]

class ActualizarCarreras(LoginRequiredMixin, UpdateView):
      model = Carreras
      success_url = "/App1/carreras/"
      fields = ["nombre", "camada"]

class EliminarCarreras(LoginRequiredMixin, DeleteView):      
      model = Carreras
      success_url = "/App1/carreras/"


class ListaEstudiantes(ListView):
      model = Estudiantes

class DetalleEstudiantes(DetailView):
      model = Estudiantes

class CrearEstudiantes(CreateView):
      model = Estudiantes
      success_url = "/App1/estudiantes/"
      fields = ["nombre", "carrera"]

class ActualizarEstudiantes(UpdateView):
      model = Estudiantes
      success_url = "/App1/estudiantes/"
      fields = ["nombre", "carrera"]

class EliminarEstudiantes(DeleteView):      
      model = Estudiantes
      success_url = "/App1/estudiantes/"
