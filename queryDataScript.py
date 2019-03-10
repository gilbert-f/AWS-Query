import boto3
from boto3.dynamodb.conditions import Key, Attr

# Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.04.html
# return exact match(es) of either one or both FirstName and LastName
def queryData(LastName, FirstName):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('css490lab4')
    results = ''
    
    print('Querying table')
    if LastName and FirstName:
        results = table.query(KeyConditionExpression=Key('LastName').eq(
            LastName) & Key('FirstName').eq(FirstName))['Items']
    elif not LastName and not FirstName:
        pass
    elif not LastName and FirstName:
        results = table.scan(FilterExpression=Key(
            'FirstName').eq(FirstName))['Items']
    elif LastName and not FirstName:
        results = table.query(KeyConditionExpression=Key(
            'LastName').eq(LastName))['Items']
    print('Table queried')
    return results

# order results in the form of "LastName FirstName attributes"
def orderKeys(results):
    outcome = []
    for result in results:
        LastName = ''
        FirstName = ''
        attributes = ''
        for key in sorted(result.keys()):
            if key == 'LastName':
                LastName = result[key]
            elif key == 'FirstName':
                FirstName = result[key]
            else:
                attributes = attributes + ' ' + str(key) + '=' + str(result[key])
        entry = LastName + ' ' + FirstName + ' ' + attributes
        outcome.append(entry)
    return outcome
