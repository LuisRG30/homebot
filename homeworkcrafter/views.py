from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages

from .models import Homework, Delivery
from.forms import RedeemForm

# Create your views here.
def index(request):
    return render(request, "homeworkcrafter/index.html")

def fee(request):
    return render(request, "homeworkcrafter/fee.html")

def redeem(request):
    
    return render(request, "homeworkcrafter/redeem.html")

def delivery(request):
    if request.method == "POST":
        code = request.POST["code"]
        try:
            delivery = Homework.objects.get(code=code)
        except Homework.DoesNotExist:
            return HttpResponseRedirect(reverse("homeworkcrafter:redeem"), {"message": "Código inválido."})
        try:
            files = Delivery.objects.get(homework=delivery)
        except Delivery.DoesNotExist:
            return render(request, "homeworkcrafter/delivery.html", {"delivery": delivery})
        context = {
            "delivery": delivery,
            "files": files
        }
        return render(request, "homeworkcrafter/delivery.html", context)

    return HttpResponseRedirect(reverse("homeworkcrafter:redeem"))
