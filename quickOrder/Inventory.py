class InventoryItem:
    def __init__(self, item_id, item_name, current_quantity, min_quantity, isOrdered, status, refillNeeded):
        self.item_id = item_id
        self.item_name = item_name
        self.current_quantity = current_quantity
        self.min_quantity = min_quantity
        self.isOrdered = isOrdered
        self.status = status
        self.refillNeeded = refillNeeded

    def needsRefill(self): 
        if (self.current_quantity < self.min_quantity):
            self.refillNeeded = True
        return self.refillNeeded

class Inventory:
    def __init__(self):
        self.inventory = []

    def addItem(self, item):
        self.inventory.append(item)
        
    def getItemName(self, item_id):
        for item in self.inventory:
            if (item.item_id == item_id)
                return item.item_name
