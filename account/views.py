from django.shortcuts import render

# Create your views here.
def renderIndex(request):
    return render(request, "../templates/layouts/index.html")

def renderLogin(request):
    return render(request, "../templates/layouts/login.html")

def renderSignUp(request):
    return render(request, "../templates/layouts/registro.html")