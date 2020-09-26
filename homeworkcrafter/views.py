from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from .models import Homework, Delivery, Message, Express
from staff.models import Review, Profile
from .forms import RedeemForm, FeeForm, MessageForm, ExpressForm
from staff.forms import ReviewForm

import secrets

import stripe

from staff.mail import *

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
            code_mail(homework=h)
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
            code_mail(homework=e)
            return render(request, "homeworkcrafter/successexpress.html", {"code": code})
        else:
            form = ExpressForm()
            context = {"message": "Algo inesperado sucedió. Es posible que se haya introcido un dato de manera erronea.", "form": form}
            return render(request, "homeworkcrafter/express.html", context)
    
    form = ExpressForm()
    return render(request, "homeworkcrafter/express.html", {"form": form})

@csrf_exempt
def stripe_config(request):
    if request.method == "GET":
        stripe_config = {"publicKey": settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == "GET":
        domain_url = "http://127.0.0.1:8000/"
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url = domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
                cancel_url = domain_url + "cancelled/",
                payment_method_types = ["card"],
                mode = "payment",
                line_items = [
                    {
                        "name": "Tarea",
                        "quantity": 1,
                        "currency": "mxn",
                        "amount": request.session["topay"],
                    }
                ]
            )
            return JsonResponse({"sessionId": checkout_session["id"]})
        except Exception as e:
            return JsonResponse({"error": str(e)})

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        # TODO: run some custom code here

    return HttpResponse(status=200)

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
                    "message": "Estamos esperando tu pago. Los detalles deben estar en tu correo electrónico.",
                    "paymentoptions": True
                }
                request.session["topay"] = delivery.price * 100
            return render(request, "homeworkcrafter/delivery.html", context)
        else:
            return render(request, "homeworkcrafter/redeem.html", {"message": "Sucedió un error."})
    form = RedeemForm()
    return render(request, "homeworkcrafter/redeem.html", {"form": form, "message": None})

def paymentsuccess(request):
    return render(request, "homeworkcrafter/paymentsuccess.html")

def paymentcancelled(request):
    return render(request, "homeworkcrafter/paymentcancelled.html")

def infohome(request):
    return render(request, "homeworkcrafter/infohome.html")

def infosecurity(request):
    return render(request, "homeworkcrafter/infosecurity.html")

def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            rating = form.cleaned_data["rating"]
            comment = form.cleaned_data["comment"]
            try:
                h = Homework.objects.get(code=code)
            except Homework.DoesNotExist:
                return render(request, "homeworkcrafter/review,html", {"message": "No existe el pedido que quieres calificar.", "form": form})
            r = Review.objects.get(homework=h)
            r.rating = rating
            r.comment = comment
            r.save()
            return render(request, "homeworkcrafter/review.html", {"message": "Recibimos tu calificación. Gracias."})
        else:
            return render(request, "homeworkcrafter/review.html", {"message": "Formulario inválido, vuelve a intentarlo."})
    form = ReviewForm()
    return render(request, "homeworkcrafter/review.html", {"form": form})

