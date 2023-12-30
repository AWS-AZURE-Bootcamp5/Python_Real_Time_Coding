import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('heydevops')
print(table.creation_date_time)

table.update_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 26
    }
)
