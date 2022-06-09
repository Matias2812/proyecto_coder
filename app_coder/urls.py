from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio),
    path("profesores" , views.profesores , name="profesores"),
    path("cursos" , views.cursos , name="cursos"),
    path("alumnos" , views.alumnos , name="alumnos" ),
    path("alta_curso" , views.curso_formulario, name="alta_curso"),
    path("buscar_curso" , views.buscar_curso, name= "buscar_curso"),
    path("alta_profesores", views.alta_profesores, name="alta_profesores"),
    path("alta_alumnos", views.alta_alumnos, name="alta_alumnos"),
    path("directivos", views.directivos, name="directivos"),
    path("alta", views.alta, name="alta"),
    path("buscar", views.buscar, name= "buscar")
]
