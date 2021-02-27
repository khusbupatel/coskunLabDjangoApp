from django.urls import path
from . import views
from . import message_views


urlpatterns = [

path('addOrder/', views.addGeneralOrder, name = 'addOrder'),
path('getOrders/', views.getGeneralOrders, name = 'getOrders'),

path('coskun/<str:order_id>/', message_views.getApproval, name = 'approval'),
path('approval/', message_views.AdminApprove, name = 'response'),

]