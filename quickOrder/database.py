from .serializers import InventoryItemSerializer
from .models import InventoryItem
from .serializers import OrderSerializer
from .models import Order
from UserManagement.models import User

def getAllInventoryObjects():
    return InventoryItem.objects.all().order_by('id')

def getInventoryObject(pk):
    return InventoryItem.objects.get(id = pk)

def updateInventoryStatus(updatedStatus, pk):
    item = getInventoryObject(pk)
    item.is_ordered = updatedStatus
    item.save() 

def updateInventoryQuantity(quantity, pk):
    item = getInventoryObject(pk)
    item.current_quantity = item.current_quantity + quantity
    item.save() 

def updateRefillNeeded(items):
    for item in items:
        if item.current_quantity < item.min_quantity:
            item.refill_needed = True
            item.save()
        if item.current_quantity > item.min_quantity:
            item.refill_needed = False
            item.save()



def getAllOrderObjects():
    return Order.objects.all().order_by('order_date', 'order_id')

def getOrderObject(pk):
    return Order.objects.get(order_id = pk)

def updateOrderStatus(updatedStatus, pk):
    order = getOrderObject(pk)
    order.status = updatedStatus
    order.save() 

def updateOrderName(pk, fk):
    item = getInventoryObject(fk)
    order = getOrderObject(pk)
    order.order_name = item.item_name
    order.save()



def getUserEmail(pk):
    return User.objects.get(id = pk).email

    