from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "homeworkcrafter/index.html")

def fee(request):
    return render(request, "homeworkcrafter/fee.html")

def redeem(request):
    return render(request, "homeworkcrafter/redeem.html")