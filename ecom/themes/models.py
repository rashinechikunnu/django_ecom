from django.db import models

# theme models.
class sitesetting(models.Model):
      banner = models.ImageField(upload_to='media/site/')
      caption = models.TextField()
