from django.db import models
from django.contrib.auth.models import User as Auth_user
from django.db.models.functions import Now


class User(models.Model):
    parent_user = models.ForeignKey(Auth_user, on_delete=models.CASCADE, null=True)
    is_landlord = models.BooleanField(default=False)  # Boolean field for landlord status
    is_student = models.BooleanField(default=False)
        
class Apartment(models.Model):
    address = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    description = models.TextField()
    dishwasher = models.BooleanField()
    washer_dryer = models.BooleanField(default = False)
    sublet = models.BooleanField()
    rent = models.IntegerField()
    move_in_date = models.DateField()
    lease_length = models.CharField(max_length = 50)
    owner = models.ForeignKey(Auth_user, on_delete=models.CASCADE)
    pets_allowed = models.BooleanField()
    num_beds = models.IntegerField()
    num_baths = models.IntegerField()
    num_sqr_ft = models.IntegerField()
    
class Message(models.Model):
    user1_id = models.ForeignKey(Auth_user, on_delete=models.CASCADE, related_name='sender')
    user2_id = models.ForeignKey(Auth_user, on_delete=models.CASCADE, related_name='receiver')
    time_sent = models.DateTimeField(db_default=Now())
    content = models.TextField()