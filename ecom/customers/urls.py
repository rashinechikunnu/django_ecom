from django.urls import path
from . import views


urlpatterns = [
    path('account',views.account_id,name='account'),
    path('logout',views.singn_out,name='logout')
] 