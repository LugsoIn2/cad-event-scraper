import os
import boto3
from src.event import Event

# Define Dynamo DB
class DBService:
    def __init__(self, key, secret):
        self.dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id=key,
            aws_secret_access_key=secret,
            region_name='eu-central-1')

    # Upload event to DynamoDB
    def upload(self, event):
        table = self.dynamodb.Table('event_table')
        item = table.put_item(Item=vars(event))
        return