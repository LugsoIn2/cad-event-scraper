import os
import boto3
from models.event import Event
from boto3.dynamodb.conditions import Key

# Define Dynamo DB
class DBService:
    def __init__(self, key, secret, ev_table_name, ten_table_name):
        self.dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id=key,
            aws_secret_access_key=secret,
            region_name='eu-central-1')
        self.ev_table_name = ev_table_name
        self.ten_table_name = ten_table_name

    # Upload event to DynamoDB
    def upload_to_event_table(self, event):
        table = self.dynamodb.Table(self.ev_table_name)
        item = table.put_item(Item=vars(event))
        return

    def get_tenants_to_fetch(self):
        table = self.dynamodb.Table(self.ten_table_name)
        response = table.query(
            IndexName='subscription_type-index',
            KeyConditionExpression=Key('subscription_type').eq(0)
        )
        
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            try:
                tenants = response['Items']
                tenants_names = list(map(lambda tenant: tenant['city'], tenants))
            except KeyError as e:
                print('Something went wrong')
            return tenants_names
        else:
            return None