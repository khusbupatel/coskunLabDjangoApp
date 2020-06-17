from .database import getInventoryObject
from .database import getOrderObject
from .database import getUserEmail

def slackMessage(pk, fk):
    blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "NEW ORDER REQUEST \n\n Item Name: " 
                    + getInventoryObject(fk).item_name 
                    + "\n Requested Quantity: " + str(getOrderObject(pk).requested_quantity)
                    + "\n Ordered By: " + str(getUserEmail(getOrderObject(pk).user.id))
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

    return blocks


def slackApprove(pk, fk):
    blocks = [{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Item Name: " 
                    + getInventoryObject(fk).item_name 
                    + "\n Requested Quantity: " + str(getOrderObject(pk).requested_quantity)
                    + "\n Ordered By: " + str(getUserEmail(getOrderObject(pk).user.id))
                    + "\n Order Date: " + str(getOrderObject(pk).order_date)
                    + "\n\n ORDER APPROVED"
                }
            }]
    return blocks

def email(pk, fk):
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
                            "item_name": getInventoryObject(fk).item_name ,
                            "requested_quantity": str(getOrderObject(pk).requested_quantity),
                            "user_name": str(getUserEmail(getOrderObject(pk).user.id)),
                            "order_date":  str(getOrderObject(pk).order_date),
                            "pk": str(pk),
                            "fk": str(fk)
                        }
                    }
                ]
        }
    return data

def slackDecline(pk, fk):
    blocks = [{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Item Name: " 
                    + getInventoryObject(fk).item_name 
                    + "\n Requested Quantity: " + str(getOrderObject(pk).requested_quantity)
                    + "\n Ordered By: " + str(getUserEmail(getOrderObject(pk).user.id))
                    + "\n Order Date: " + str(getOrderObject(pk).order_date)
                    + "\n\n ORDER Declined"
                }
            }]
    return blocks