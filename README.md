# awsLambda

   Lambda allows you to define various triggers which can be hundreds of different events provided by dozens of different event sources. In our case, we’re going to use the S3 event provider. Events are being fired all of the time in S3 from new files  that are uploaded to buckets (incoming bucket),Print data of files and files being copy to processed bucket.
   
   To deploy, Serverless framework required a aws accesskey and secretkey. Which can be set by below command 
   
      serverless config credentials --provider aws --key <<KEY>> --secret <<SECRET>>

### Deployment

To deploy this application , need not to create any resource on aws. Deployment will handle all of required resources.To start deployment need to execute below command at command prompt.
      
        sls deploy

### How to Test

  Upload one file to "incominglambda" bucket, that has the subscribed event, this should automatically kick off the Lambda function. To confirm this, head over to CloudWatch or click on the Monitoring tab inside of the function itself. This initial view shows a lot of great information about the function’s execution. Testing file "testS3data.txt" is also in this repository.
  
  Log output would looks like :-
  
      START RequestId: 495c1fd6-9c71-4061-9e8f-41759d576dcc Version: $LATEST
      START Printing contents of file -> testS3data.txt
      Hi
      my name is sumit
      testing my S3 trigger on lambda -> CloudWatch log
      END Printing contents of file -> testS3data.txt
      START Transfering file -> testS3data.txt to bucket processedlambda
      END Transfering file -> testS3data.txt to bucket processedlambda


### To remove deployment

To remove deployment just need to execute below command 

      sls remove
      
### Additional all S3 bucket clenup command

In order to make it proper running , have to do many time clean all S3 bucket. Same would also required when we did many round of test and now time to remove all test files. To cleanup S3 bucket need to to go to aws. Have added one plugin "serverless-s3-remover". Using below command can install it ...

      npm install serverless-s3-remover

Cleanup command :- When we're removing our deployemnt , this plugin also doing cleanup...

      sls s3remove

Go to S3 service using Service -> search S3. Now need to create two buckets - incominglambda & processedlambda. During creating bucket keep all defaults settings.
We'll use incominglambda bucket to upload files and after printing , files will be copied into processedlambda bucket.

When executed, Lambda needs to have permission to access your S3 bucket. Before we get started building our Lambda function, we must first create an IAM role( or assign policy to existing user) which Lambda will use to work with S3.
   
#### S3 Buckets 
   Right now both bucket "incominglambda" & "processedlambda" are hardcoded into lambda handler. We can make it configurable too.
      in this example , hardcoded inbucket and out bucket name. We can also dynamically refer inbucket name as
   
         inbucket = j['s3']['bucket']['name']
   
   Same way file, if we want to trigger from SNS event and have to read SNS message we can use like 
   
         import ast
         sns_message = ast.literal_eval(j['Sns']['Message'])
  
