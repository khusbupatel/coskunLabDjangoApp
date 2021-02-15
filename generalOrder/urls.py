from django.urls import path
from . import views


urlpatterns = [

path('addOrder/', views.addGeneralOrder, name = 'addOrder'),
path('getOrders/', views.getGeneralOrders, name = 'getOrders')

]