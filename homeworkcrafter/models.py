import os
from django.conf import settings
from django.db import models


# Create your models here.
class Homework(models.Model):
    homework = models.CharField(max_length=64)
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    number = models.CharField(max_length=32)
    level = models.CharField(max_length=32, default="bachillerato")
    subject = models.CharField(max_length=64)
    date = models.DateField()
    description = models.CharField(max_length=5000)
    instruction_file = models.FileField(null = True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    code = models.CharField(max_length=16, unique=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.homework}, {self.subject}, {self.date}, {self.price}]"

class Delivery(models.Model):
    homework = models.OneToOneField(Homework, on_delete=models.CASCADE, primary_key=True, related_name="delivery")
    deliveredfile = models.FileField(null=True)

    def __str__(self):
        return f"[Code: {self.homework.code}, Paid: {self.homework.paid}]"

"""    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.deliveredfile.name))
        super(Delivery, self).delete(*args, **kwargs)"""

class Message(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    message = models.CharField(max_length=5000)