import json
import boto3

#in out buckets 
inbucket = 'incominglambda'
outbucket = 'processedlambda'
s3 = boto3.client('s3',aws_access_key_id='ACCESS_KEY',aws_secret_access_key='SECRET_ACCESS')


def lambda_handler(event, context):
    for j in event['Records']:
        s3_filename = j['s3']['object']['key']
        data = s3.get_object(Bucket=inbucket,Key=s3_filename)
        contents = data['Body'].read().decode()
        print('START Printing contents of file ->',s3_filename)
        print(contents)
        print('END Printing contents of file ->',s3_filename)
        print('START Transfering file ->',s3_filename,' to bucket processedlambda')
        copy_source = {'Bucket':inbucket, 'Key':s3_filename}
        s3.copy_object(Bucket=outbucket, Key=s3_filename, CopySource=copy_source)
        print('END Transfering file ->',s3_filename,' to bucket processedlambda')
    return {
        'statusCode': 200,
        'body': json.dumps('File Printed and Processed!')
    }
