from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def code_mail(name, email, code):
    subject = "Recibimos tu Pedido"
    html_message = render_to_string("staff/codemail.html", {"name": name, "code": code})
    plain_message = strip_tags(html_message)
    from_email = "homeworkcrafter@gmail.com"
    to = email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)

def price_mail(name, email, price, account):
    pass

def delivery_mail(name, email):
    subject = "Tu pedido está listo"
    html_message = render_to_string("staff/deliverymail.html", {"name": name})
    plain_message = strip_tags(html_message)
    from_email = "homeworkcrafter@gmail.com"
    to = email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)