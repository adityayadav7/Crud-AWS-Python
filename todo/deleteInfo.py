import json
import boto3

dynamodb= boto3.resource('dynamodb')

def delete(event,context):

    table=dynamodb.Table('informations')

    table.delete_item(
        Key={
            'id':event['pathParameters']['id']
        }
    )

    response={
        "statusCode":200,
        "body":json.dumps("deleted succesfully")
        
    }

    return response
