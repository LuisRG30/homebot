from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages

from .models import Homework, Delivery
from.forms import RedeemForm, FeeForm

# Create your views here.
def index(request):
    return render(request, "homeworkcrafter/index.html")

def fee(request):
    if request.method == "POST":
        form = FeeForm(request.POST)
        if form.is_valid():
            homework = form.cleaned_data["homework"]
            email = form.cleaned_data["email"]
            number = form.cleaned_data["number"]
            level = form.cleaned_data["level"]
            subject = form.cleaned_data["subject"]
            date = form.cleaned_data["date"]
            instruction_file = form.cleaned_data["instruction_file"]
            description = form.cleaned_data["description"]
            h = Homework(homework=homework, email=email, number=number, level=level, subject=subject, date=date, instruction_file=instruction_file, description=description)
            h.save()
            return render(request, "homeworkcrafter/successfee.html")

    form = FeeForm()
    return render(request, "homeworkcrafter/fee.html", {"form": form})

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
            try:
                files = Delivery.objects.get(homework=delivery)
            except Delivery.DoesNotExist:
                return render(request, "homeworkcrafter/delivery.html", {"delivery": delivery})
            context = {
                "delivery": delivery,
                "files": files
            }
            return render(request, "homeworkcrafter/delivery.html", context)
        else:
            return render(request, "homeworkcrafter/redeem.html", {"message": "Sucedió un error."})
    form = RedeemForm()
    return render(request, "homeworkcrafter/redeem.html", {"form": form})

