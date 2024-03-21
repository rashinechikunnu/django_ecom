from django.db import models

# product model

class product(models.Model):
      LIVE = 1
      DELETE = 0
      DELETE_CHOICES = ((LIVE,'live'),(DELETE,'delete'))
      title = models.CharField(max_length=250)
      price = models.FloatField()
      description = models.TextField()
      image = models.ImageField(upload_to='media/')
      priority = models.IntegerField(default=0)
      delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
      create_at = models.DateTimeField(auto_now_add= True)
      update_at = models.DateTimeField(auto_now = True)


      def __str__(self):
            return self.title

