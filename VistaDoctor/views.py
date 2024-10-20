from django.shortcuts import render, redirect
from account import models
# Create your views here.

def vistaListaCitas(request):
    citas = models.Citas.objects.all()
    for cita in citas:
        print(cita.tratamiento)
        print(cita.paciente.last_name)
        print(cita.paciente.first_name)
    if request.method == 'GET':
        return render(request, "../templates/layouts/lista-citas.html", {
            'citas':  citas
        })
