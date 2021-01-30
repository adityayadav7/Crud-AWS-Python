import json

import boto3
from todo import decimalencoder

dynamodb=boto3.resource('dynamodb')

def list(event,context):
    table=dynamodb.Table('informations')

    result=table.scan()

    response={
        "statusCode":200,
        "body":json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }
    return response