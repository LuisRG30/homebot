from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "welcome/index.html")

def fee(request):
    return render(request, "welcome/fee.html")