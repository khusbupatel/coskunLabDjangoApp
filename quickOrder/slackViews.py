from slack import WebClient

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.conf import settings
slackClient = WebClient('xoxb-1151661690016-1129336370418-4BsG7WYoVlAjpgWXcLNDp2no')

@api_view(['POST'])
def getProfApproval(request):

    slackClient.chat_postMessage(
        channel = '#project',
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "NEW ORDER REQUEST \n 'Order Details here'"
                }
            },
            {
                "type": "actions",
                "block_id": "actionblock789",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Approve"
                        },
                        "style": "primary",
                        "value": "aprrove_button"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Decline"
                        },
                        "style": "danger",
                        "value": "decline_button"
                    }
                    
                ]
            }
        ]
    )

    return Response( status = status.HTTP_200_OK )

@api_view(['POST'])
def sendToFinance(request):

    slackClient.chat_postMessage(
        channel = '#finance',
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "NEW ORDER REQUEST \n 'Order Details here'"
                }
            },
            {
                "type": "actions",
                "block_id": "actionblock789",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Ordered"
                        },
                        "style": "primary",
                        "value": "order_button"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Cancelled"
                        },
                        "style": "danger",
                        "value": "cancel_button"
                    }
                    
                ]
            }
        ]
    )

    return Response( status = status.HTTP_200_OK )


@api_view(['POST'])
def followUpFinance(request):

    slackClient.chat_postMessage(
        channel = '#finance',
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "ORDER REQUEST \n 'Order Details here'"
                }
            },
            {
                "type": "actions",
                "block_id": "actionblock789",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Delivered"
                        },
                        "style": "primary",
                        "value": "deliver_button"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Cancelled"
                        },
                        "style": "danger",
                        "value": "cancel_button"
                    }
                    
                ]
            }
        ]
    )

    return Response( status = status.HTTP_200_OK )

# add POST for button requests

