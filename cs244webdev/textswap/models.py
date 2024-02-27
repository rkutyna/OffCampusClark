from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
class Apartment(models.Model):
    address = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='apartment')
    description = models.TextField()
    dishwasher = models.BooleanField()
    sublet = models.BooleanField()
    rent = models.IntegerField()
    move_in_date = models.DateField()
    lease_length = models.CharField(max_length = 50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pets_allowed = models.BooleanField()
    num_beds = models.IntegerField()
    num_baths = models.IntegerField()
    num_sqr_ft = models.IntegerField()