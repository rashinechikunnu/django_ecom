from django.db import models
from customers.models import customer
from products.models import product



# data models for order.
class order(models.Model):
      LIVE = 1
      DELETE = 0
      DELETE_CHOICES = ((LIVE,'live'),(DELETE,'delete'))

      CART_STAGE = 0
      ODER_CONFIRMED = 1
      ODER_PROCESSED = 2
      ODER_DELIVERED = 3
      ODER_REJECTED = 4
      STATUS_CHOICE = ((ODER_PROCESSED,'ODER_PROCESSED'),
                       (ODER_DELIVERED,'ODER_DELIVERED'),
                       (ODER_REJECTED,'ODER_REJECTED'))
      oder_status = models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)

      owner = models.ForeignKey(customer,on_delete = models.SET_NULL,null=True, related_name='oders')
      delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
      create_at = models.DateTimeField(auto_now_add= True)
      update_at = models.DateTimeField(auto_now = True)

# model order items
class ordereditem(models.Model):
      product = models.ForeignKey(product,related_name='added_carts',on_delete=models.SET_NULL,null=True)
      quantity = models.IntegerField(default=1)
      owner = models.ForeignKey(order,on_delete=models.CASCADE,related_name='add_items')

