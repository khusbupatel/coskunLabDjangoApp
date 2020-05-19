from .serializers import InventoryItemSerializer
from .models import InventoryItem
from .serializers import OrderSerializer
from .models import Order

def getAllInventoryObjects():
    return InventoryItem.objects.all()

def getInventoryObject(pk):
    return InventoryItem.objects.get(id = pk)

def getAllOrderObjects():
    return Order.objects.all().order_by('order_date', 'order_id')

def getOrderObject(pk):
    return Order.objects.get(order_id = pk)


