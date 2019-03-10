import boto3

# Reference: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.delete_objects
# clear bucket
def clearBucket():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('css490lab4s3')
    
    print('Clearing bucket')
    bucket.delete_objects(Delete = {'Objects': [{'Key': 'input.txt'}]})
    print('Bucket cleared')

# Reference: https://gist.github.com/Swalloow/9966d576a9aafff482eef6b59c222baa
# clear dynamoDB table
def clearTable():
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('css490lab4')
        
    print('Clearing table')
    for item in table.scan()['Items']:
        # print(str(item['LastName']) + ' ' + str(item['FirstName']) + ' deleted...') # for debugging
        table.delete_item(Key={'LastName': str(item['LastName']), 'FirstName': str(item['FirstName'])})
    print('Table cleared')
