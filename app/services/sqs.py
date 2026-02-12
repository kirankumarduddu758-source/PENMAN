import boto3
import os
import json

region = os.getenv("AWS_REGION", "us-east-1")
sqs = boto3.client("sqs", region_name=region)

QUEUE_URL = os.getenv("QUEUE_URL", "")

def send_event(message: dict):
    if not QUEUE_URL:
        return

    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(message)
    )
