from django.shortcuts import render,redirect
from .models import order,ordereditem
# Create your views here.

def show_cart(request):
      return render(request,'cart_show.html')


def add_to_cart(request):
      if request.POST:
            user=request.user
            customers=user.customer
            quantity =int(request.POST.get('quantity'))
            product_id=request.POST.get('product_id')
            card_obj,crated = order.objects.get_or_create(
                  onwer = customers,
                  order_status = order.CART_STAGE
            )

            order_item =ordereditem.objects.create(
                  product = product_id,
                  owner = card_obj,
                  quantity = quantity
            )


      return redirect('cart')
