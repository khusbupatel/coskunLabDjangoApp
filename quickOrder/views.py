from django.http import JsonResponse
from django.shortcuts import render
from django.http import Http404 
from rest_framework import status

# third party imports
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import InventoryItemSerializer
from .models import InventoryItem
from .utilities import getAllInventoryObjects
from .utilities import getInventoryObject


@api_view(['GET'])
def getInventory(request):
    items = getAllInventoryObjects()
    serializer = InventoryItemSerializer(items, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = InventoryItemSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def getItem(request, pk):
    item = getInventoryObject(pk)
    serializer = InventoryItemSerializer(item, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateItem(request, pk):
    item = getInventoryObject(pk)
    serializer = InventoryItemSerializer(instance = item, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteItem(request, pk):
    item = getInventoryObject(pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

