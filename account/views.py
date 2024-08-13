from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
# Create your views here.
def renderIndex(request):
    return render(request, "../templates/layouts/index.html")

def Login(request):
    if request.method == 'GET':
        return render(request, "../templates/layouts/login.html")
    else:
        user = authenticate(request, username = request.POST['correo'], password = request.POST['contraseña'])
        if user is None:
            return render(request, 'login')
        else:
            login(request, user)
            return redirect("Index")
            

def SignUp(request):
    if request.method == 'GET':
        return render(request, "../templates/layouts/registro.html")
    else:
        if request.method == 'POST':
            try:
                newUser = User.objects.create_user(username=request.POST['correo'], password=request.POST['contraseña'], email=request.POST['correo'], first_name = request.POST['nombres'], last_name = request.POST['apellidos'])
                newUser.save()
                login(request, newUser)
                print("Se guardo de forma correcta")
                return redirect('Index')
            except:
                return render(request, 'singup.html')
            
def signOut(request):
    logout(request)
    return redirect("Index")