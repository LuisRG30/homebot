from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages

from homeworkcrafter.models import Homework, Delivery
from staff.models import Profile

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("staff:login"))
    context = {
        "homeworks": Homework.objects.all()
    }
    return render(request, "staff/index.html", context)

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

def homework(request, homework_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("staff:login"))
    try: 
        homework = Homework.objects.get(pk=homework_id)
    except Homework.DoesNotExist:
        raise Http404("Homework does not exist")
    context = {
        "homework": homework
    }
    request.session["job"] = homework_id
    return render(request, "staff/homework.html", context)

def addjob(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("staff:login"))
    if request.method == "POST":
        homework_id = request.session["job"]
        profile = Profile.objects.get(user=request.user)
        profile.job = Homework.objects.get(pk=homework_id)
        profile.save()
        return render(request, "staff/addjob.html")
    return HttpResponseRedirect(reverse("staff:index"))

def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("staff:login"))
    user = request.user
    profile = Profile.objects.get(user=user)
    context = {
        "user": user,
        "profile": profile
    }
    return render(request, "staff/profile.html", context)

def assignment(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("staff:login"))
    profile = Profile.objects.get(user=request.user)
    job = profile.job
    if job is not None:
        return render(request, "staff/assignment.html", {"homework": job})
    else:
        return HttpResponseRedirect(reverse("staff:profile"))