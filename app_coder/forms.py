from django import forms


class Curso_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()


class Alumno_formulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()
    nacimiento = forms.DateField()

class Profesor_formulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()
    fecha_alta= forms.DateTimeField()
    dicta_materia= forms.CharField(max_length=20)
    email = forms.CharField(max_length=40)

