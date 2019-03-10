# AWS-Query
A simple Python Flask web app using AWS's S3, DynamoDB, Elastic Beanstalk, and EC2.

How to use
1.	When the “Load Data” button is hit the website will load data from an object stored at a given URL. First the data is copied into an S3 bucket. Then, it is parsed and loaded into a <Key, Value> NoSQL table (Dynamo DB). Note that the load button can be hit multiple times. Each time the test file will be parsed, and the NoSQL DB will be updated.
2.	When the “Clear Data” button is hit the S3 object is removed from the bucket. The NoSQL table is also emptied.
3.	Once the data has been loaded in the NoSQL table the user can type in either one or both first name and last name. When the “Query Data” button is hit, results are shown on a table. For querying, the names should be exact matches. Note that you do not need to fill in both query boxes to query.
