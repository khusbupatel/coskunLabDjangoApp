from django.http import JsonResponse
from django.shortcuts import render
from django.http import Http404 
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import OrderSerializer
from .models import Order
from .database import getAllOrderObjects
from .database import updateOrderName
from .messageViews import getProfApproval


# Called on Submit Request
@api_view(['POST'])
def addOrder(request):
    serializer = OrderSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        getProfApproval(request._request, serializer.data.get("item_id"), serializer.data.get("order_id"))
        updateOrderName(serializer.data.get("order_id"), serializer.data.get("item_id"))
        return Response(serializer.data, status = status.HTTP_200_OK)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# View Order Table on frontend side
@api_view(['GET'])
def getOrders(request):
    items = getAllOrderObjects()
    serializer = OrderSerializer(items, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['DELETE'])
def deleteOrder(request, pk):
    item = getOrderObject(pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


