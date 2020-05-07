from rest_framework import serializers

from .models import InventoryItem
from django import forms

# transformation from model to json
class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'