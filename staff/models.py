from django.db import models


from django.contrib.auth.models import User
from homeworkcrafter.models import Homework

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    job = models.OneToOneField(Homework, null=True, blank=True, on_delete=models.SET_NULL, related_name="worker")
    role = models.CharField(max_length=32, default="Colaborador")
    

    def __str__(self):
        return f"{self.user} working on {self.job}"

class Review(models.Model):
    homework = models.OneToOneField(Homework, null=True, on_delete=models.SET_NULL, related_name="review")
    worker = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="review")
    rating = models.IntegerField(null=True, blank=True)
    comment = models.CharField(max_length=5000, null=True, blank=True)