from django.db import models

# Create your models here.

class Post(models.Model):
    item_name = models.CharField(max_length = 50)
    current_quantity = models.IntegerField()
    min_quantity = models.IntegerField()
    isOrdered = models.BooleanField(default = False)
    status = models.TextField(blank = True)

    def __str__(self):
        return self.item_name