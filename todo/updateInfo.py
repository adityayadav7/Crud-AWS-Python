import json
import time
import logging
import boto3
from todo import decimalencoder

dynamodb = boto3.resource('dynamodb')

def update(event,context):
    data = json.loads(event['body'])
    if 'text' not in data or 'checked' not in data:
        logging.error("something wrong")
        raise Exception("Couldn't update the info ")
        return

    timestamp = int(time.time()*1000)
    table=dynamodb.Table('informations')

    result=table.update_item(
        Key={
            'id':event['pathParameters']['id']
        },
        ExpressionAttributeNames={
            '#info_text': 'text',
        },
        UpdateExpression= "set #info_text = :t, checked = :c, updateAt = :u",
        ExpressionAttributeValues={
            ':t': data['text'],
            ':c': data['checked'],
            ':u': timestamp

        },
        ReturnValues="UPDATED_NEW"

    )
    response = {
        "statusCode":200,
        "body": json.dumps(result['Attributes'], cls=decimalencoder.DecimalEncoder)
    }

    return response
