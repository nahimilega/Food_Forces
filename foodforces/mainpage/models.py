from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class user(models.Model):
    user_name=models.CharField(max_length=250)
    user_email=models.CharField(max_length=250)    
    def __str__(self):
        return self.user_name




class order(models.Model):
    
    resturant_name=models.CharField(max_length=2500)
    offer_description=models.CharField(max_length=2500)
    #mobile_no=models.BigIntegerField()
    Target_value=models.IntegerField()
    #Waiting_time=

    def get_absolute_url(self):
        return reverse("mainpage:index")
    
    