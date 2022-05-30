from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.shortcuts import render
from django.template.loader import get_template

def bienvenida(request):
    familiares=["Marta","Silvana","María","Exequiel","Gonzalo"]
    return render (request,'Base.html', {'nombre': 'Vane','apellido':'Dominguez','familiares':familiares})

