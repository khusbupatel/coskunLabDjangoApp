from slack import WebClient

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
from django.shortcuts import redirect

from .models import Order
from .database import getInventoryObject
from .database import getOrderObject
from .database import updateOrderStatus
from .database import updateInventoryStatus
from .database import updateInventoryQuantity

from mailjet_rest import Client
import os

api_key = '36eb38a2e21cbd237ca510f857f15d7e'
api_secret = '96638375a5627dcbd0f7ec38276fb616'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

slackClient = WebClient('xoxb-1151661690016-1129336370418-DNYHkj2nkci7xEIwIlu0PM5V')

@api_view(['POST'])
def getProfApproval(request, fk, pk):

    slackClient.chat_postMessage(
        channel = '#project',
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "NEW ORDER REQUEST \n\n Item Name: " 
                    + getInventoryObject(fk).item_name 
                    + "\n Requested Quantity: " + str(getOrderObject(pk).requested_quantity)
                    + "\n Ordered By: " + str(getOrderObject(pk).user)
                    + "\n Order Date: " + str(getOrderObject(pk).order_date)
                }
            },
            {
                "type": "actions",
                "block_id": "coskun" + ":" + str(fk) + ":" + str(pk),
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Approve"
                        },
                        "action_id": "Approve",
                        "style": "primary",
                        "value": "aprrove_button"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Decline"
                        },
                        "action_id": "Decline",
                        "style": "danger",
                        "value": "decline_button"
                    }
                    
                ]
            }
        ]
    )

    return Response(status = status.HTTP_200_OK )

@api_view(['POST'])
def CoskunApprove(request):
    check = json.loads(request.POST.get("payload"))
    buttonName = check.get("actions")[0].get("text").get("text")
    pk_fk = check.get("actions")[0].get("block_id").split(":")

    if buttonName == 'Approve':
        updateOrderStatus("Approved", pk_fk[2])
        slackClient.chat_update(
            channel = "C013RQ9F0RG",
            ts = check.get("message").get("ts"),
            blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Item Name: " 
                    + getInventoryObject(pk_fk[1]).item_name 
                    + "\n Requested Quantity: " + str(getOrderObject(pk_fk[2]).requested_quantity)
                    + "\n Ordered By: " + str(getOrderObject(pk_fk[2]).user)
                    + "\n Order Date: " + str(getOrderObject(pk_fk[2]).order_date)
                    + "\n\n ORDER APPROVED"
                }
            }
            ]
        )

        data = {
            'Messages': [
                    {
                        "From": {
                            "Email": "kpatel607@gatech.edu",
                            "Name": "Coskun Lab"
                        },
                        "To": [
                            {
                                "Email": "patelparadise39@gmail.com",
                                "Name": "Finance"
                            }
                        ],
                        "TemplateID": 1476639,
                        "TemplateLanguage": True,
                        "Subject": "New Order Request",
                        "Variables": {
                            "item_name": getInventoryObject(pk_fk[1]).item_name ,
                            "requested_quantity": str(getOrderObject(pk_fk[2]).requested_quantity),
                            "user_name": str(getOrderObject(pk_fk[2]).user),
                            "order_date":  str(getOrderObject(pk_fk[2]).order_date),
                            "pk": str(pk_fk[2]),
                            "fk": str(pk_fk[1])
                        }
                    }
                ]
        }
        result = mailjet.send.create(data=data)

    if buttonName == 'Decline':
        updateOrderStatus("Declined", pk_fk[2])
        slackClient.chat_update(
            channel = "C013RQ9F0RG",
            ts = check.get("message").get("ts"),
            blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Item Name: " 
                    + getInventoryObject(pk_fk[1]).item_name 
                    + "\n Requested Quantity: " + str(getOrderObject(pk_fk[2]).requested_quantity)
                    + "\n Ordered By: " + str(getOrderObject(pk_fk[2]).user)
                    + "\n Order Date: " + str(getOrderObject(pk_fk[2]).order_date)
                    + "\n\n ORDER Declined"
                }
            }
            ]
        )

    return Response(status = status.HTTP_200_OK)

@api_view(['GET'])
def FinanceApprove(request, pk, fk):
    if (getOrderObject(pk).status == "Approved"):
        updateOrderStatus("Ordered", pk)
        updateInventoryStatus(True, fk)
        return redirect('http://localhost:3000/inventory/')
    return Response(status = status.HTTP_200_OK)

@api_view(['GET'])
def FinanceDeliver(request, pk, fk):
    if (getOrderObject(pk).status == "Ordered"):
        updateOrderStatus("Delivered", pk)
        updateInventoryStatus(False, fk)
        updateInventoryQuantity(getOrderObject(pk).requested_quantity, fk)        
    return redirect('http://localhost:3000/inventory/')

@api_view(['GET'])
def FinanceCancel(request, pk, fk):
    if (getOrderObject(pk).status == "Approved" or getOrderObject(pk).status == "Ordered"):
        updateOrderStatus("Cancelled", pk)
        updateInventoryStatus(False, fk)
    return redirect('http://localhost:3000/inventory/')



