from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here.

class EstudianteFormulario (forms.Form):
    nombre = forms.CharField(max_length=50)
    carrera = forms.CharField(max_length=30)

class CarreraFormulario (forms.Form):
    nombre = forms.CharField(max_length=50)
    camada = forms.IntegerField()

class ProfesorFormulario (forms.Form):
    nombre = forms.CharField(max_length=50)
    carrera = forms.CharField(max_length=30)

class UsuarioRegistro (UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class FormularioEditar(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]