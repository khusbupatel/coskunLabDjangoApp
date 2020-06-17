from slack import WebClient

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
from django.shortcuts import redirect

from .models import Order

from .database import getOrderObject
from .database import updateOrderStatus
from .database import updateInventoryQuantity

from .messages import slackMessage
from .messages import slackApprove
from .messages import email
from .messages import slackDecline

from mailjet_rest import Client
import os

# SLACK AND MAILJET CREDENTIALS
api_key = 'XXX'
api_secret = 'XXX'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

slackClient = WebClient('XXX')

@api_view(['POST'])
def getProfApproval(request, fk, pk):
    slackClient.chat_postMessage(
        channel = '#project',
        blocks = slackMessage(pk, fk)
    )

    return Response(status = status.HTTP_200_OK )

@api_view(['POST'])
def CoskunApprove(request):
    check = json.loads(request.POST.get("payload"))
    buttonName = check.get("actions")[0].get("text").get("text")
    fk_pk = check.get("actions")[0].get("block_id").split(":")

    if buttonName == 'Approve':
        updateOrderStatus("Approved", fk_pk[2])
        slackClient.chat_update(
            channel = "C013RQ9F0RG",
            ts = check.get("message").get("ts"),
            blocks = slackApprove(fk_pk[2], fk_pk[1])
        )

        data = email(fk_pk[2], fk_pk[1])
        result = mailjet.send.create(data=data)

    if buttonName == 'Decline':
        updateOrderStatus("Declined", fk_pk[2])
        slackClient.chat_update(
            channel = "C013RQ9F0RG",
            ts = check.get("message").get("ts"),
            blocks = slackDecline(fk_pk[2], fk_pk[1])
        )

    return Response(status = status.HTTP_200_OK)

@api_view(['GET'])
def FinanceApprove(request, pk, fk):
    if (getOrderObject(pk).status == "Approved"):
        updateOrderStatus("Ordered", pk)
        return redirect('http://localhost:3000/inventory/')
    return Response(status = status.HTTP_200_OK)

@api_view(['GET'])
def FinanceDeliver(request, pk, fk):
    if (getOrderObject(pk).status == "Ordered"):
        updateOrderStatus("Delivered", pk)
        updateInventoryQuantity(getOrderObject(pk).requested_quantity, fk)        
        return redirect('http://localhost:3000/inventory/')
    return Response(status = status.HTTP_200_OK)

@api_view(['GET'])
def FinanceCancel(request, pk, fk):
    if (getOrderObject(pk).status == "Approved" or getOrderObject(pk).status == "Ordered"):
        updateOrderStatus("Cancelled", pk)
        return redirect('http://localhost:3000/inventory/')
    return Response(status = status.HTTP_200_OK)




