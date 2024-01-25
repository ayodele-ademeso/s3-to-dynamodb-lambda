# Movie Catalogue Lambda Function

This AWS Lambda function is designed to read a CSV file from an S3 bucket, process its content, and insert the records into a DynamoDB table. The DynamoDB table has a primary key named 'ID', and the 'Rating' attribute is stored as a Decimal.

## Functionality

1. **Input:**
   - The Lambda function is triggered by an S3 event whenever a new CSV file is uploaded to a specific bucket.

2. **Processing:**
   - The Lambda function reads the CSV content from the S3 bucket.
   - Parses the CSV content and extracts 'Title', 'Year', 'Genre', and 'Rating' fields.
   - Generates a unique 'ID' for each record based on 'Title' and 'Year'.
   - Inserts the records into a DynamoDB table.

3. **Output:**
   - Returns a response with information about the insertion operation:
     - A message indicating success.
     - A list of items inserted during the current execution.
     - A list of all items in the DynamoDB table after the insertions.

## Configuration

### Environment Variables
   - **AWS_S3_BUCKET:** Specify the name of the S3 bucket where CSV files are stored.
   - **AWS_S3_BUCKET_KEY:** Specify the key (path) of the CSV file within the S3 bucket.
   - **table_name:** Specify the name of the DynamoDB table.

### IAM Role Permissions
   - Ensure that the Lambda function's IAM role has the necessary permissions:
     - `s3:GetObject` for reading from S3.
     - `dynamodb:PutItem` for inserting items into DynamoDB.
     - Additional permissions as needed.

## Usage

1. Create an S3 bucket to store your CSV files.
2. Create a DynamoDB table with the required attributes, including the primary key 'ID'.
3. Configure the Lambda function with the necessary environment variables and IAM role permissions.
4. Deploy the Lambda function.
5. Upload a CSV file to the specified S3 bucket.

## Dependencies

- [boto3](https://github.com/boto/boto3): The Amazon Web Services (AWS) SDK for Python.
