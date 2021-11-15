from django.db import models


class Register(models.Model):
    email= models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class SignUp(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    address = models.CharField(max_length=200)