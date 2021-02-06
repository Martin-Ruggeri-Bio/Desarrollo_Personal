from django.http import HttpResponse
import datetime
# from django.template.loader import get_template
from django.shortcuts import render


class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


# primera vista
def saludo(request):
    p1 = Persona("Martin", "Ruggeri")
    ahora = datetime.datetime.now()
    temas_del_curso = [
        "Plantillas", "Modelos", "Formularios",
        "Vistas", "Despliegue"
    ]
    # doc_ext = get_template('mi_plantilla.html')
    dic = {
        "nombre_mio": p1.nombre,
        "apellido_mio": p1.apellido,
        "momento_actual": ahora,
        "temas": temas_del_curso}
    # documento = doc_ext.render(dic)
    return render(request, "mi_plantilla.html", dic)


def cursoWs(request):
    fecha_actual = datetime.datetime.now()
    dic = {"dameFecha": fecha_actual}
    return render(request, "cursoWs.html", dic)


def cursoPy(request):
    fecha_actual = datetime.datetime.now()
    dic = {"dameFecha": fecha_actual}
    return render(request, "cursoPy.html", dic)


def despedida(request):
    return HttpResponse("Hata luego usuario de Django")


def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html><body><h1>
                    Fecha y hora actuales %s
                <h1><body><html>""" % fecha_actual
    return HttpResponse(documento)


def calculaEdad(request, edad, agno):
    periodo = agno - 2020
    edadFutura = edad + periodo
    documento = """<html><body><h1>
                    En el año %s tendras %s años
                <h1><body><html>""" % (agno, edadFutura)
    return HttpResponse(documento)
