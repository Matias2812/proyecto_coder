from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Alumno, Curso, Profesores
from django.template import loader
from app_coder.forms import Curso_formulario, Profesor_formulario, Alumno_formulario
# Create your views here.


def inicio(request):

    return render( request , "plantillas.html" )

def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos" : cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

def alumnos(request):

    alumnos = Alumno.objects.all()
    dicc = {"alumno" : alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )


def directivos(request):

    return render( request , "directivos.html" )


def profesores(request):

    profesores = Profesores.objects.all()
    dicc = {"profesores" : profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento ) 


#Alta del curso
def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            curso = Curso( nombre=datos['nombre'] , camada=datos['camada'])
            curso.save()

            return render( request , "formulario.html")

    return render( request, "formulario.html")

def buscar_curso(request):

    return render( request , "buscar_curso.html")



def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")
   


def alta_profesores(request):

    if request.method == "POST":

        mi_formulario = Profesor_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            profesor = Profesores( nombre=datos['nombre'] , legajo=datos['legajo'], fecha_alta= datos['fecha_alta'], dicta_materia=datos['dicta_materia'], email=datos['email'] )
            profesor.save()

        return render(request, "alta_profesores.html")
    
    return render( request, "alta_profesores.html")

def alta_alumnos(request):

    if request.method == "POST":

        mi_formulario = Alumno_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            alumno = Alumno( nombre=datos['nombre'] , camada=datos['camada'], nacimiento=datos['nacimiento'])
            alumno.save()

            return render( request , "formulario.html")

    return render( request, "alta_alumnos.html")

def alta(request):
    return render(request, "alta.html")