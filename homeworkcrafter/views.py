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
    form = forms.Feeform()
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

