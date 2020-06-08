from django.urls import path

from . import views
from . import orderViews
from . import slackViews

urlpatterns = [
    path('inventory/', views.getInventory, name = 'inventory'),
    path('add-item/', views.addItem, name = 'add-item'),
    path('get-item/<str:pk>/', views.getItem, name = 'get-item'),
    path('update-item/<str:pk>/', views.updateItem, name = 'update-item'),
    path('delete-item/<str:pk>/', views.deleteItem, name = 'delete-item'),

    path('orders/', orderViews.getOrders, name = 'orders'),
    path('add-order/', orderViews.addOrder, name = 'add-order'),
    path('get-order/<str:pk>/', orderViews.getOrder, name = 'get-order'),
    path('update-order/<str:pk>/', orderViews.updateOrder, name = 'update-order'),
    path('delete-order/<str:pk>/', orderViews.deleteOrder, name = 'delete-order'),
    
    path('coskun/<str:fk>/<str:pk>/', slackViews.getProfApproval, name = 'Dr. Coskun'),
    path('approval/', slackViews.CoskunApprove, name = 'approval'),
    path('financeApproval/<str:pk>/<str:fk>/', slackViews.FinanceApprove, name = 'Finance approval'),
    path('financeDeliver/<str:pk>/<str:fk>/', slackViews.FinanceDeliver, name = 'Finance Deliver'),
    path('financeCancel/<str:pk>/<str:fk>/', slackViews.FinanceCancel, name = 'Finance Cancel')


]
