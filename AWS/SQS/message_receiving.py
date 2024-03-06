import boto3

# Configure the AWS credentials and endpoint for LocalStack
sqs = boto3.client('sqs',
                   region_name='us-east-1',
                   endpoint_url='http://localhost:4566',
                   aws_access_key_id='YOUR_ACCESS_KEY_ID',
                   aws_secret_access_key='YOUR_SECRET_ACCESS_KEY')

queue_url = 'http://localhost:4566/000000000000/sync_profile_q'  # Queue URL for localstack

response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1
)

messages = response.get('Messages', [])
print(messages)

for message in messages:
    print("Received message:", message)

    # Delete the message from the queue
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=message['ReceiptHandle']
    )