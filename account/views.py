from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from . import models
# Create your views here.
def renderIndex(request):
    return render(request, "../templates/layouts/index.html")

def Login(request):
    if request.method == 'GET':
        return render(request, "../templates/layouts/login.html")
    else:
        usera = authenticate(request, username = request.POST['correo'], password = request.POST['contraseña'])
        if usera is None:
            return render(request, "../templates/layouts/login.html")
        else:
            try:
                extra_info = models.ExtraInfo.objects.get(user=usera)
                if(extra_info.rol == 2):
                    return redirect("VistaDoctor:ListaCitas")
                else:
                    login(request, usera)
                    return redirect("VistaDoctor:ListaCitas")
            except models.ExtraInfo.DoesNotExist:
                return redirect("login")
            

def SignUp(request):
    if request.method == 'GET':
        return render(request, "layouts/registro.html")
    elif request.method == 'POST':
        try:
            # Crear un nuevo usuario
            newUser = User.objects.create_user(
                username=request.POST['correo'],
                password=request.POST['contraseña'],
                email=request.POST['correo'],
                first_name=request.POST['nombres'],
                last_name=request.POST['apellidos']
            )

            # Obtener rol por defecto o el que necesites
            default_rol = models.Roles.objects.get(id=1)  # Asumiendo que '1' es el rol deseado

            # Crear la información adicional del usuario
            extrainfo = models.ExtraInfo.objects.create(
                user=newUser,
                numero_celular=request.POST['celular'],
                birth_date=request.POST['fecha_nacimiento'],
                rol=default_rol
            )

            # Guardar y autenticar al nuevo usuario
            newUser.save()
            login(request, newUser)
            print("Se guardó de forma correctad")

            # Redirigir a la página de inicio
            return redirect('Index')

        except Exception as e:
            print(f"Error: {e}")  # Esto puede ayudar a depurar en caso de errores
            return render(request, 'layouts/registro.html', {'error': 'Hubo un error al crear la cuenta. Inténtalo de nuevo.'})
            
def signOut(request):
    logout(request)
    return redirect("Index")