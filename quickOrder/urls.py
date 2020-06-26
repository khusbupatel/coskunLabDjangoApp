from django.urls import path

from . import views
from . import order_views
from . import message_views

urlpatterns = [
    path('inventory/', views.getInventory, name = 'inventory'),
    path('add-item/', views.addItem, name = 'add-item'),
    path('update-item/<str:item_id>/', views.updateItem, name = 'update-item'),
    path('delete-item/<str:item_id>/', views.deleteItem, name = 'delete-item'),

    path('orders/', order_views.getOrders, name = 'orders'),
    path('add-order/', order_views.addOrder, name = 'add-order'),
    path('delete-order/<str:order_id>/', order_views.deleteOrder, name = 'delete-order'),
    
    path('coskun/<str:order_id>/<str:item_id>/', message_views.getProfApproval, name = 'Dr. Coskun'),
    path('approval/', message_views.CoskunApprove, name = 'approval'),
    path('financeApproval/<str:order_id>/', message_views.FinanceApprove, name = 'Finance approval'),
    path('financeDeliver/<str:order_id>/<str:item_id>/', message_views.FinanceDeliver, name = 'Finance Deliver'),
    path('financeCancel/<str:order_id>/', message_views.FinanceCancel, name = 'Finance Cancel')


]
