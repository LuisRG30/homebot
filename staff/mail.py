from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def code_mail(homework):
    subject = "Recibimos tu Pedido"
    context = {
        "homework": homework.homework,
        "name": homework.name,
        "code": homework.code,
        "subject": homework.subject,
        "date": homework.date,
        "time": homework.time,
        "description": homework.description
    }
    html_message = render_to_string("staff/codemail.html", context)
    plain_message = strip_tags(html_message)
    from_email = "homeworkcrafter@gmail.com"
    to = homework.email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)

def price_mail(homework, account):
    subject = "Puedes proceder con el pago"
    context = {
        "homework": homework.homework,
        "name": homework.name,
        "code": homework.code,
        "subject": homework.subject,
        "date": homework.date,
        "time": homework.time,
        "description": homework.description,
        "price": homework.price,
        "account": account
    }
    html_message = render_to_string("staff/pricemail.html", context)
    plain_message = strip_tags(html_message)
    from_email = "homeworkcrafter@gmail.com"
    to = homework.email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)

def delivery_mail(name, email):
    subject = "Tu pedido está listo"
    html_message = render_to_string("staff/deliverymail.html", {"name": name})
    plain_message = strip_tags(html_message)
    from_email = "homeworkcrafter@gmail.com"
    to = email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)