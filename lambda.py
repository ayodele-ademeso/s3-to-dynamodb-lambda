import boto3
import csv
from io import StringIO
from decimal import Decimal

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table_name = 'movie-catalogue-db'
AWS_S3_BUCKET = 'ayodele-csv-bucket'
AWS_S3_BUCKET_KEY = 'movies.csv'

def lambda_handler(event, context):
    # Get the S3 bucket and key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Download the CSV file from S3
    response = s3.get_object(Bucket=AWS_S3_BUCKET, Key=AWS_S3_BUCKET_KEY)
    csv_content = response['Body'].read().decode('utf-8')

    # Parse CSV content
    csv_reader = csv.DictReader(StringIO(csv_content))
    csv_rows = list(csv_reader)

    # Connect to DynamoDB table
    dynamodb_table = dynamodb.Table(table_name)
    
    inserted_items = []

    # Iterate through CSV rows and insert into DynamoDB
    for row in csv_rows:
        # Generate a unique 'ID' for each record (you can modify this logic as needed)
        record_id = f"{row['Title']}_{row['Year']}"

        # Insert record into DynamoDB
        dynamodb_table.put_item(
            Item={
                'ID': record_id,
                'Title': row['Title'],
                'Year': int(row['Year']),
                'Genre': row['Genre'],
                'Rating': Decimal(row['Rating'])
            }
        )
        
        # Append inserted item to the list
        inserted_items.append({
            'ID': record_id,
            'Title': row['Title'],
            'Year': int(row['Year']),
            'Genre': row['Genre'],
            'Rating': Decimal(row['Rating'])
        })

    # Query DynamoDB to get all items in the table
    query_result = dynamodb_table.scan()


    return {
        'statusCode': 200,
        'body': {
            'message': 'DynamoDB insertion and query successful',
            'inserted_items': inserted_items,
            'all_items': query_result['Items']
        }
    }
