from slack import WebClient

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json

from .models import Order
from .utilities import getInventoryObject
from .utilities import getOrderObject
from .utilities import updateOrderStatus
from .utilities import updateInventoryStatus
from .utilities import updateInventoryQuantity

slackClient = WebClient('XXX')

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
def sendToFinance(request, fk, pk):

    slackClient.chat_postMessage(
        channel = '#finance',
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
                "block_id": "finance" + ":" + str(fk) + ":" + str(pk),
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Ordered"
                        },
                        "action_id": "Ordered",                       
                        "style": "primary",
                        "value": "order_button"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Cancelled"
                        },
                        "action_id": "Cancelled",                       
                        "style": "danger",
                        "value": "cancel_button"
                    }
                    
                ]
            }
        ]
    )

    return Response( status = status.HTTP_200_OK )


@api_view(['POST'])
def followUpFinance(request, fk, pk):

    slackClient.chat_postMessage(
        channel = '#finance',
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "ORDER REQUEST \n\n Item Name: " 
                    + getInventoryObject(fk).item_name 
                    + "\n Requested Quantity: " + str(getOrderObject(pk).requested_quantity)
                    + "\n Ordered By: " + str(getOrderObject(pk).user)
                    + "\n Order Date: " + str(getOrderObject(pk).order_date)
                }
            },
            {
                "type": "actions",
                "block_id": "followUp" + ":" + str(fk) + ":" + str(pk),
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Delivered"
                        },
                        "action_id": "Delivered",                        
                        "style": "primary",
                        "value": "deliver_button"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Cancelled"
                        },
                        "action_id": "Cancelled",                         
                        "style": "danger",
                        "value": "cancel_button"
                    }
                    
                ]
            }
        ]
    )

    return Response(status = status.HTTP_200_OK )

# add POST for button requests


@api_view(['POST'])
def CoskunApprove(request):
    check = json.loads(request.POST.get("payload"))
    buttonName = check.get("actions")[0].get("text").get("text")
    pk_fk = check.get("actions")[0].get("block_id").split(":")

    if buttonName == 'Approve':
        sendToFinance(request._request, pk_fk[1], pk_fk[2])
        updateOrderStatus("Approved", pk_fk[2])
        slackClient.chat_update(
            channel = "C013RQ9F0RG",
            ts = check.get("message").get("ts"),
            blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Order Approved" 
                }
            }
            ]
        )

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
                    "text": "Order has been declined" 
                }
            }
            ]
        )

    if buttonName == 'Ordered':
        followUpFinance(request._request, pk_fk[1], pk_fk[2])
        updateOrderStatus("Ordered", pk_fk[2])
        slackClient.chat_update(
            channel = "C0143E4HD1S",
            ts = check.get("message").get("ts"),
            blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Order has been ordered" 
                }
            }
            ]
        )
        updateInventoryStatus(True, pk_fk[1])


    if buttonName == 'Cancelled':
        updateOrderStatus("Cancelled", pk_fk[2])
        slackClient.chat_update(
            channel = "C0143E4HD1S",
            ts = check.get("message").get("ts"),
            blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Order has been cancelled" 
                }
            }
            ]
        )
        updateInventoryStatus(False, pk_fk[1])



    if buttonName == 'Delivered':
        updateOrderStatus("Delivered", pk_fk[2])
        slackClient.chat_update(
            channel = "C0143E4HD1S",
            ts = check.get("message").get("ts"),
            blocks = [
            {

                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Order has been delivered" 
                }
            }
            ]
        )
        updateInventoryStatus(False, pk_fk[1])
        updateInventoryQuantity(getOrderObject(pk_fk[2]).requested_quantity, pk_fk[1])        


    return Response(status = status.HTTP_200_OK)
