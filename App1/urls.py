
from django.urls import path
from App1.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name= "Inicio"),
    path('estudiantes/', estudiante, name="Estudiantes"),
    path('carreras/', carrera, name="Carreras"),
    path('profesores/', profesor, name="Profesores"),
    path('carreraFormulario/', carreraFormulario, name="FormularioCarrera"),
    path('buscarCamada/', busquedaCamada , name="BuscarCamada"),
    path('resultados/', resultados , name="Resultados"),
    path('login/', inicioSesion , name="Login"),
    path('register/', registro , name="Register"),
    path('logout/', LogoutView.as_view(template_name="App1/logout.html"), name="Logout"),
    path('editar/', editarUsuario , name="EditarUsuario"),
    

# CRUD DE PROFESORES
    path('leerProfesores/', leerProfesores , name="leerProfesores"),
    path('crearProfesores/', crearProfesores , name="crearProfesores"),
    path('eliminarProfesores/<profesorNombre>/', eliminarProfesores , name="eliminarProfesores"),
    path('editarProfesores/<profesorNombre>/', editarProfesores , name="editarProfesores"),

#CRUD DE CARRERAS USANDO CLASES
    path('carreras/list', ListaCarreras.as_view(), name="CarrerasLeer"),
    path('carreras/<int:pk>', DetalleCarreras.as_view(), name="CarrerasDetalle"),
    path('carreras/crear/', CrearCarreras.as_view(), name="CarrerasCrear"),
    path('carreras/editar/<int:pk>', ActualizarCarreras.as_view(), name="CarrerasEditar"),
    path('carreras/eliminar/<int:pk>', EliminarCarreras.as_view(), name="CarrerasEliminar"),

#CRUD DE ESTUDIANTES USANDO CLASES
    path('estudiantes/list', ListaEstudiantes.as_view(), name="EstudiantesLeer"),
    path('estudiantes/<int:pk>', DetalleEstudiantes.as_view(), name="EstudiantesDetalle"),
    path('estudiantes/crear/', CrearEstudiantes.as_view(), name="EstudiantesCrear"),
    path('estudiantes/editar/<int:pk>', ActualizarEstudiantes.as_view(), name="EstudiantesEditar"),
    path('estudiantes/eliminar/<int:pk>', EliminarEstudiantes.as_view(), name="EstudiantesEliminar"),

]
 