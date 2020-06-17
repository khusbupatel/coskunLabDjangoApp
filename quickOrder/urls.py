from django.urls import path

from . import views
from . import orderViews
from . import messageViews

urlpatterns = [
    path('inventory/', views.getInventory, name = 'inventory'),
    path('add-item/', views.addItem, name = 'add-item'),
    path('update-item/<str:pk>/', views.updateItem, name = 'update-item'),
    path('delete-item/<str:pk>/', views.deleteItem, name = 'delete-item'),

    path('orders/', orderViews.getOrders, name = 'orders'),
    path('add-order/', orderViews.addOrder, name = 'add-order'),
    path('delete-order/<str:pk>/', orderViews.deleteOrder, name = 'delete-order'),
    
    path('coskun/<str:fk>/<str:pk>/', messageViews.getProfApproval, name = 'Dr. Coskun'),
    path('approval/', messageViews.CoskunApprove, name = 'approval'),
    path('financeApproval/<str:pk>/<str:fk>/', messageViews.FinanceApprove, name = 'Finance approval'),
    path('financeDeliver/<str:pk>/<str:fk>/', messageViews.FinanceDeliver, name = 'Finance Deliver'),
    path('financeCancel/<str:pk>/<str:fk>/', messageViews.FinanceCancel, name = 'Finance Cancel')


]
