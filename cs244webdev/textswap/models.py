from django.db import models
from django.contrib.auth.models import User as Auth_user
from django.db.models.functions import Now
from datetime import datetime
import os



class User(models.Model):
    parent_user = models.ForeignKey(Auth_user, on_delete=models.CASCADE, null=True)
    is_landlord = models.BooleanField(default=False)  # Boolean field for landlord status
    is_student = models.BooleanField(default=False)
    
def get_upload_path(instance, filename):
    return os.path.join('textswap/static/images', filename)
        
class Apartment(models.Model):
    address = models.CharField(max_length=100)
    #photo = models.ImageField(upload_to='textswap/static/images')
    photo_name = models.CharField(max_length=100, default=None)  # New field to store the photo name
    photo = models.ImageField(upload_to=get_upload_path)  # Use a custom function for upload_to
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
    
    def save(self, *args, **kwargs):
        if not self.photo_name:
            original_filename = os.path.basename(self.photo.name)
            self.photo_name = original_filename.replace(' ', '_')
        print(self.photo_name)
        super().save(*args, **kwargs)
    
class Message(models.Model):
    user1_id = models.ForeignKey(Auth_user, on_delete=models.CASCADE, related_name='sender')
    user2_id = models.ForeignKey(Auth_user, on_delete=models.CASCADE, related_name='receiver')
    time_sent = models.DateTimeField(default=datetime.now)
    content = models.TextField()