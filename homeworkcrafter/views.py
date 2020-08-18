from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages

from .models import Homework, Delivery, Message, Express
from .forms import RedeemForm, FeeForm, MessageForm, ExpressForm

import secrets

# Create your views here.
def index(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            m = Message(name=name, email=email, message=message)
            m.save()
    form = MessageForm()
    return render(request, "homeworkcrafter/index.html", {"form": form})

def fee(request):
    if request.method == "POST":
        form = FeeForm(request.POST, request.FILES)
        if form.is_valid():
            homework = form.cleaned_data["homework"]
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            number = form.cleaned_data["number"]
            level = form.cleaned_data["level"]
            subject = form.cleaned_data["subject"]
            date = form.cleaned_data["date"]
            time = form.cleaned_data["time"]
            description = form.cleaned_data["description"]
            code = secrets.token_hex(6)
            h = Homework(homework=homework, name=name, email=email, number=number, level=level, subject=subject, date=date, time=time, description=description, code=code, instruction_file=form.cleaned_data["file"])
            h.save()
            return render(request, "homeworkcrafter/successfee.html", {"code": code})
        else:
            form = FeeForm()
            context = {"message": "Algo inesperado sucedió. Es posible que se haya introcido un dato de manera erronea.", "form": form}
            return render(request, "homeworkcrafter/fee.html", context)

    form = FeeForm()
    return render(request, "homeworkcrafter/fee.html", {"form": form})

def express(request):
    if request.method == "POST":
        form = ExpressForm(request.POST)
        if form.is_valid():
            homework = form.cleaned_data["homework"]
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            number = form.cleaned_data["number"]
            level = form.cleaned_data["level"]
            subject = form.cleaned_data["subject"]
            date = form.cleaned_data["date"]
            time = form.cleaned_data["time"]
            description = form.cleaned_data["description"]
            code = secrets.token_hex(6)
            e = Express(homework=homework, name=name, email=email, number=number, level=level, subject=subject, date=date, time=time, description=description, code=code, instruction_file=form.cleaned_data["file"])
            e.save()
            return render(request, "homeworkcrafter/successexpress.html", {"code": code})
        else:
            form = ExpressForm()
            context = {"message": "Algo inesperado sucedió. Es posible que se haya introcido un dato de manera erronea.", "form": form}
            return render(request, "homeworkcrafter/express.html", context)
    
    form = ExpressForm()
    return render(request, "homeworkcrafter/express.html", {"form": form})

def redeem(request):
    if request.method == "POST":
        form = RedeemForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            try:
                delivery = Homework.objects.get(code=code)
            except Homework.DoesNotExist:
                form = RedeemForm()
                context = {
                    "message": "Código inválido.",
                    "form": form
                }
                return render(request, "homeworkcrafter/redeem.html", context)
            if delivery.paid == True:
                try:
                    files = Delivery.objects.get(homework=delivery)
                except Delivery.DoesNotExist:
                    return render(request, "homeworkcrafter/delivery.html", {"delivery": delivery, "message": "Descarga no disponible todavía."})
                context = {
                    "delivery": delivery,
                    "doc": files
                }
            else:
                context = {
                    "delivery": delivery,
                    "message": "Estamos esperando tu pago."
                }
            return render(request, "homeworkcrafter/delivery.html", context)
        else:
            return render(request, "homeworkcrafter/redeem.html", {"message": "Sucedió un error."})
    form = RedeemForm()
    return render(request, "homeworkcrafter/redeem.html", {"form": form, "message": None})

def infohome(request):
    return render(request, "homeworkcrafter/infohome.html")

def infoexpress(request):
    return render(request, "homeworkcrafter/infoexpress.html")

