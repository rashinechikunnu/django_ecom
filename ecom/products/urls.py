from django.urls import path
from . import views
urlpatterns=[
      path("home",views.index,name='home'),
      path('product',views.produts,name='product_list'),
      path('details_product/<pk>',views.product_details,name='details_product')
]