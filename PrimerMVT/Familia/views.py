from django.shortcuts import render
from Familia.models import Familiares, Sobre_mi
from django.template import Template, Context

# Create your views here.
def datos_familiares (request):
    f_1= Familiares.objects.create (
        nombre= 'Marta',
        edad = 78,
        parentesco = 'Mamá',
        email= 'mom@mom.com',
        telefono= '4123456',
        f_nacimiento = '1944-4-14'
        )
    f_2= Familiares.objects.create (
        nombre= 'Silvana',
        edad = 44,
        parentesco = 'Hermana',
        email= 'sil@sil.com',
        telefono= '41345',
        f_nacimiento = '1978-8-5'
        )
    f_3= Familiares.objects.create (
        nombre= 'María',
        edad = 42,
        parentesco = 'Hermana',
        email= 'maria@maria.com',
        telefono= '41987',
        f_nacimiento = '1980-5-6'
        )
    f_4= Familiares.objects.create (
        nombre= 'Gonzalo',
        edad = 40,
        parentesco = 'Hermano',
        email= 'gon@gon.com',
        telefono= '43568',
        f_nacimiento = '1982-5-22'
        )

    f_5= Familiares.objects.create (
        nombre= 'Exequiel',
        edad = 34,
        parentesco = 'Hermano',
        email= 'exe@exe.com',
        telefono= '487756',
        f_nacimiento = '1988-1-13'
        )


    return render(request,'Familiares.html',{'f_1':f_1,'f_2':f_2,'f_3':f_3,'f_4':f_4,'f_5':f_5})

def datos_personales (request):
    persona= Sobre_mi.objects.create(
        nombre= 'Vanessa',
        edad = 37,
        email= 'vane@vane.com',
        telefono= '15234689',
        f_nacimiento = '1984-11-17'
        )
    return render (request,'Sobre_mi.html',{'persona':persona})