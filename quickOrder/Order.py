class Order():
    def __init__(self, order_id, item_id, status, requested_quantity, order_date):
        self.order_id = order_date
        self.item_id = item_id
        self.status = status
        self.requested_quantity = requested_quantity
        self.order_date = order_date

    def getOrderItemName(self, inventory): 
        return getItemName(inventory, self.item_id)
        