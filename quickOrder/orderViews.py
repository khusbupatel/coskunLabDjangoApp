from django.http import JsonResponse
from django.shortcuts import render
from django.http import Http404 
from django.core.exceptions import ObjectDoesNotExist

# third party imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import OrderSerializer
from .models import Order
from .utilities import getAllOrderObjects
from .utilities import getOrderObject


# Called on Submit Request
@api_view(['POST'])
def addOrder(request):
    serializer = OrderSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# View Order Table on frontend side
@api_view(['GET'])
def getOrders(request):
    items = getAllOrderObjects()
    serializer = OrderSerializer(items, many = True)
    return Response(serializer.data)

# Need for Slack calls
@api_view(['GET'])
def getOrder(request, pk):
    item = getOrderObject(pk)
    serializer = OrderSerializer(item, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateOrder(request, pk):
    item = getOrderObject(pk)
    serializer = Orderserializer(instance = item, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteOrder(request, pk):
    item = getOrderObject(pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


