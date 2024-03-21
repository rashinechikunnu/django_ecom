from django.db import models
from django.contrib.auth.models import User
# customer model

class customer(models.Model):
      LIVE = 1
      DELETE = 0
      DELETE_CHOICES = ((LIVE,'live'),(DELETE,'delete'))
      name = models.CharField(max_length=250)
      address = models.TextField()
      user= models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer')
      phone = models.CharField(max_length=10)
      delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
      create_at = models.DateTimeField(auto_now_add= True)
      update_at = models.DateTimeField(auto_now = True)


      def __str__(self):
            return self.name
