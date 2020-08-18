from django.contrib import admin

from .models import Homework, Delivery, Message, Express

# Register your models here.

admin.site.register(Homework)
admin.site.register(Delivery)
admin.site.register(Message)
admin.site.register(Express)