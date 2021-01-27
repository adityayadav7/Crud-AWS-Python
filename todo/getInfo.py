import json 
import boto3

dynamodb=boto3.resource('dynamodb')

def getInfoById(event,context):
    table=dynamodb.Table('informations')

    result= table.get_item(
        Key={
            'id':event['pathParameters']['id']
        }
    )

    response={
        "statusCode":200,
        "body":json.dumps(result['Item'])
    }

    return response