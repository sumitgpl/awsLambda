# awsLambda

   Lambda allows you to define various triggers which can be hundreds of different events provided by dozens of different event sources. In our case, we’re going to use the S3 event provider. Events are being fired all of the time in S3 from new files  that are uploaded to buckets (incoming bucket),Print data of files and files being copy to processed bucket.

### Setting up S3

Go to S3 service using Service -> search S3. Now need to create two buckets - incominglambda & processedlambda. During creating bucket keep all defaults settings.
We'll use incominglambda bucket to upload files and after printing , file will be copied into processedlambda bucket.

When executed, Lambda needs to have permission to access your S3 bucket. Before we get started building your Lambda function, you must first create an IAM role( or assign policy to existing user) which Lambda will use to work with S3.

### Creating the Lambda Function

#### Adding Code
   Once you have the role/user set up, you’ll then need to create the lambda function. To do that, you’ll browse to Lambda and click Create Function. Creating a new Lambda function, I’ll be using Python 3.7 as the run-time.

   Our example code isn’t going to do much. It will only prove that it ran when an S3 event happen. In the example below, I’m using the builtin event Python dictionary and referencing the S3 key that initiated the event and printing it out. This output will show up in the CloudWatch Logs. Copy all code from "lambda_function.py" from this same repository and place to "Function Code" block.
   
#### Adding the Trigger

   Once we've the code we’ll be using inside of the function, we’ll then create the S3 trigger be selecting it on the left-hand side. Since we want to trigger off of new uploads, we’ll create this event to trigger off of the PUT event.


### Time to Test 

  Upload one file to "incominglambda" bucket, that has the subscribed event, this should automatically kick off the Lambda function. To confirm this, head over to CloudWatch or click on the Monitoring tab inside of the function itself. This initial view shows a lot of great information about the function’s execution. 
  
  Log output would looks like 
  
    START RequestId: bfaba56c-9405-427d-8ece-030a8c3f0f19 Version: $LATEST
    START Printing contents of file -> testS3data.txt
    Hi
    my name is sumit

    testing my S3 trigger on lambda -> CloudWatch log
    END Printing contents of file -> testS3data.txt
    START Transfering file -> testS3data.txt to bucket processedlambda
    END Transfering file -> testS3data.txt to bucket processedlambda
    END RequestId: bfaba56c-9405-427d-8ece-030a8c3f0f19
    REPORT RequestId: bfaba56c-9405-427d-8ece-030a8c3f0f19 Duration: 474.79 ms Billed Duration: 500 ms Memory Size: 128 MB Max Memory Used: 81 MB Init Duration: 375.67 ms 
