from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User as Auth_user
from django.db.models.functions import Now
from datetime import datetime
from django.conf import settings
import os



class User(models.Model):
    parent_user = models.ForeignKey(Auth_user, on_delete=models.CASCADE, null=True)
    is_landlord = models.BooleanField(default=False)  # Boolean field for landlord status
    is_student = models.BooleanField(default=False)
    
def get_upload_path(instance, filename):
    image_path = os.path.join(str(instance.apartment_id.id), filename)
    return image_path
        
"""class Apartment(models.Model):
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
        #print(self.photo_name)
        super().save(*args, **kwargs)"""
    
class Message(models.Model):
    user1_id = models.ForeignKey(Auth_user, on_delete=models.CASCADE, related_name='sender')
    user2_id = models.ForeignKey(Auth_user, on_delete=models.CASCADE, related_name='receiver')
    time_sent = models.DateTimeField(default=datetime.now)
    content = models.TextField()

class Apartment(models.Model):
    address = models.CharField(unique=True)
    description = models.TextField()
    dishwasher = models.BooleanField()
    washer_dryer = models.BooleanField(default = False)
    sublet = models.BooleanField()
    rent = models.DecimalField(decimal_places=2, max_digits=10)
    move_in_date = models.DateField()
    lease_length = models.CharField()
    owner = models.ForeignKey(Auth_user, on_delete=models.CASCADE)
    pets_allowed = models.BooleanField()
    num_beds = models.IntegerField(validators=[MinValueValidator(0)])
    num_baths = models.IntegerField(validators=[MinValueValidator(0)])
    num_sqr_ft = models.IntegerField(validators=[MinValueValidator(0)])
    
class Photo(models.Model):
    apartment_id = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    # The photo name and photo url are separate because django uses different directories when storing the 
    # photo and when attempting to access the photo, so this code in addition to get_upload_path() and save()
    # ensures that the photos are saved to the correct location
    photo_name = models.CharField(default=None)  # New field to store the photo name
    photo = models.ImageField(upload_to=get_upload_path)  # Use a custom function for upload_to
    
    def save(self, *args, **kwargs):
        if not self.photo_name:
            original_filename = os.path.basename(self.photo.name)
            self.photo_name = original_filename.replace(' ', '_')
        print("\n \n \n", self.photo_name, "\n \n \n")
        print(settings.MEDIA_ROOT)
        super().save(*args, **kwargs)