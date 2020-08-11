from django.db import models

# Create your models here.
class Homework(models.Model):
    homework = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    number = models.CharField(max_length=32)
    subject = models.CharField(max_length=64)
    date = models.DateField()
    description = models.CharField(max_length=5000)
    price = models.IntegerField(blank=True)
    code = models.CharField(max_length=16)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.homework}, {self.subject}, {self.date}, {self.price}]"

class Delivery(models.Model):
    homework = models.OneToOneField(Homework, on_delete=models.CASCADE, primary_key=True)
    deliveredfile = models.FileField(null=True)

    def __str__(self):
        return f"[Code: {self.homework.code}, Paid: {self.homework.paid}]"