from .serializers import InventoryItemSerializer
from .models import InventoryItem

def getAllObjects():
    return InventoryItem.objects.all()

def getObject(pk):
    return InventoryItem.objects.get(id = pk)


