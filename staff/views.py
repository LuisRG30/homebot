from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseBadRequest
from django.urls import reverse
from django.contrib import messages

from homeworkcrafter.models import Homework, Delivery
from staff.models import Profile
from .forms import DeliveryForm, LoginForm 

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("staff:login"))
    context = {
        "homeworks": Homework.objects.filter(worker=None, delivery=None, paid=False)
    }
    return render(request, "staff/index.html", context)

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.username
            password = form.password
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("staff:index"))
            else:
                form = LoginForm()
                context = {
                    "message": "Usuario o contraseña incorrectos.",
                    "form": form
                }
                return render(request, "staff/login.html", context)
    else:
        form = LoginForm()
        return render(request, "staff/login.html", {"form": form})

def logout_view(request):
    logout(request)
    form = LoginForm()
    context = {
        "message": "Sesión cerrada exitosamente.",
        "form": form
    }
    return render(request, "staff/login.html", context)

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
        return HttpResponseRedirect(reverse("staff:profile"))
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
        form = DeliveryForm()
        return render(request, "staff/assignment.html", {"homework": job, "form": form})
    else:
        return HttpResponseRedirect(reverse("staff:profile"))

def submit(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("staff:login"))
    if request.method == "POST":
        form = DeliveryForm(request.POST, request.FILES)
        if form.is_valid():
            worker = Profile.objects.get(user=request.user)
            homework = Homework.objects.get(worker=worker)
            d = Delivery(homework=homework, deliveredfile=form.cleaned_data["file"])
            d.save()
            worker.job = None
            worker.save()
            return HttpResponseRedirect(reverse("staff:profile"))
        else:
            return HttpResponseBadRequest(content="Unexpected error.")
    return HttpResponseRedirect(reverse("staff:profile"))
