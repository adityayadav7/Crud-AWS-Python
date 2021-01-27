import json

import boto3

dynamodb=boto3.resource('dynamodb')

def list(event,context):
    table=dynamodb.Table('informations')

    result=table.scan()

    response={
        "statusCode":200,
        "body":json.dumps(result['Items'])
    }
    return response