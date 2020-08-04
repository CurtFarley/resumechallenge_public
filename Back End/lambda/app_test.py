import boto3
import dynamo_helper
import smtplib

dynamo_client = boto3.resource('dynamodb')
client = boto3.client('sns')
# def lambda_handler(event, context):
#     dynamo_helper.update_table('test_Visitors', 'VisitorCount', 'vc')


# if __name__ == '__main__':
#     lambda_handler(None, None)

def get_count(table, pk, column):
    dynamodb = boto3.resource('dynamodb')
    table = dynamo_client.Table(table)
    response = table.get_item(
            Key={pk: 1}
        )
    count = response['Item'][column]
    print(response)
    print ("count is", count)

    return(count)

# get_count('test_Visitors', 'VisitorCount', 'vc')

# def lambda_handler(evelont, context):
#     dynamo_helper.update_table('test_Visitors', 'VisitorCount', 'vc')



older_value = get_count('test_Visitors','VisitorCount', 'vc')
dynamo_helper.update_table('test_Visitors', 'VisitorCount', 'vc')
newer_value = get_count('test_Visitors','VisitorCount', 'vc')

def email_error():
    s = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com')

    s.connect('email-smtp.us-east-1.amazonaws.com', '587')

    s.starttls()
    s.login('AKIARMP73ALTNY2K25GJ', 'BDaAjBgJpwGe3Mr+J0h8RcKfUEB2/eNjx0TjbOzBPMBm')

    msg = 'From: daniel.ksingletary@gmail.com\nTo: dan.ksingletary@gmail.com\nSubject: Test Email\n\nThis is an error message, your script failed miserably!'

    s.sendmail('daniel.ksingletary@gmail.com', 'dan.ksingletary@gmail.com', msg)
    return()


assert newer_value == older_value + 1, email_error()
    
