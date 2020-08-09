from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("staff:login"))
    return render(request, "staff/index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("staff:index"))
        else:
            return render(request, "staff/login.html", {
                "message": "Usuario o contraseña incorrectos."
            })
    else:
        return render(request, "staff/login.html")

def logout_view(request):
    logout(request)
    return render(request, "staff/login.html",{
        "message": "Sesión cerrada exitosamente."
    })