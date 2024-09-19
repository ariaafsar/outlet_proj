from django.db import models
from django.contrib.auth.models import User

class Provider(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)

    def __str__(self):
        self.user.username

class Customer(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)

    def __str__(self):
        self.user.username


# Create your models here.
