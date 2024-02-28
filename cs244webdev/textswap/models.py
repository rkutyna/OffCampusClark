from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_landlord = models.BooleanField(default=False)  # Boolean field for landlord status
    is_student = models.BooleanField(default=False)