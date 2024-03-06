import json
import boto3

# Configure the AWS credentials and endpoint for LocalStack
sqs = boto3.client('sqs',
                   region_name='us-east-1',
                   endpoint_url='http://localhost:4566',
                   aws_access_key_id='YOUR_ACCESS_KEY_ID',
                   aws_secret_access_key='YOUR_SECRET_ACCESS_KEY')

queue_url = 'http://localhost:4566/000000000000/sync_profile_q'  # Queue URL for localstack

json_data = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 3
}

# Convert JSON data to a string
message_body = json.dumps(json_data)

message_attributes = {
    'Version': {
        'DataType': 'String',
        'StringValue': '1.0'  # Adjust the version number as needed
    }
}

response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=message_body,
    MessageAttributes=message_attributes
)

print("Message sent! MessageId:", response['MessageId'])