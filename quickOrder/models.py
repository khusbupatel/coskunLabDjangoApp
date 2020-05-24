from django.db import models
from django.utils import timezone

# Create your models here.

class InventoryItem(models.Model):
    item_name = models.CharField(max_length = 50)
    current_quantity = models.IntegerField()
    min_quantity = models.IntegerField()
    refillNeeded = models.BooleanField(default = False)
    isOrdered = models.BooleanField(default = False)

    def __str__(self):
        return self.item_name

class Order(models.Model):
    order_id = models.AutoField(primary_key = True, unique = True)
    item_id = models.ForeignKey(InventoryItem, on_delete = models.CASCADE)
    status = models.TextField(default = "Pending Approval")
    requested_quantity = models.IntegerField(default = 0)
    order_date = models.DateTimeField(default = timezone.now)
    user = models.TextField()
    
    def __str__(self):
        return self.status