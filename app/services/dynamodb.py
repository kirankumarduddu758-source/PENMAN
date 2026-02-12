import boto3
import os
from datetime import datetime

region = os.getenv("AWS_REGION", "us-east-1")
dynamodb = boto3.resource("dynamodb", region_name=region)

TABLE_NAME = os.getenv("TABLE_NAME", "penman-data")

def get_table():
    return dynamodb.Table(TABLE_NAME)


def save_registration(data: dict):
    table = get_table()

    item = {
        "PK": f"USER#{data['phone']}",
        "SK": f"REG#{datetime.utcnow().isoformat()}",
        **data
    }

    table.put_item(Item=item)


def save_contact(data: dict):
    table = get_table()

    item = {
        "PK": "CONTACT",
        "SK": f"MSG#{datetime.utcnow().isoformat()}",
        **data
    }

    table.put_item(Item=item)
