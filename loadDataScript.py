import boto3

# Reference: https://stackoverflow.com/questions/47468148/how-to-copy-s3-object-from-one-bucket-to-another-using-python-boto3/47468350
# copy s3 object from other bucket to my bucket
def copyData():
    s3 = boto3.resource('s3')
    copy_source = {
        'Bucket': 'css490',
        'Key': 'input.txt'
    }
    bucket = s3.Bucket('css490lab4s3')
    
    print('Copying s3 object')
    bucket.copy(copy_source, 'input.txt')
    print('s3 object copied')

# Reference: https://stackoverflow.com/questions/31976273/open-s3-object-as-a-string-with-boto3
# read s3 object from my bucket and return the string equivalent
def readData():
    s3 = boto3.resource('s3')
    obj = s3.Object('css490lab4s3', 'input.txt')
    
    print('s3 object decoded')
    return obj.get()['Body'].read().decode('ascii')

# Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html
# parse string from readData() to dynamoDB items with key value pairs
def parseData():
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('css490lab4')
    items = readData().splitlines()
    
    # parse each line (item) to key value pairs
    print('Putting items')
    for item in items:
        attributes = item.split()
        i = 0
        parsedItem = {}
        for attribute in attributes:
            if i == 0:
                parsedItem['LastName'] = attribute
            elif i == 1:
                parsedItem['FirstName'] = attribute
            else:
                key, value = attribute.split('=')
                parsedItem[key] = value
            i = i + 1
        table.put_item(Item = parsedItem)
    print('Items put')
