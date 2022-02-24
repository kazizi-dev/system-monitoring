# system-monitoring-design
System monitoring with the help of Elastic ELK stack, AWS, and Docker.

### Motivation:
Build a system that can answer business and technical related questions for 
engineering and customer support teams in order to better assist clients.

### Objectives:
1. Design real-time and scheduled data processign solutions that collect and aggregate data.
2. Build a system that can alert the team about problems and anomalies on Slack.
3. Create an automated ticketing system on Jira.

### Design 1:
1. Install a Logstash image in a docker container and run the container using an EC2
instance on AWS cloud to continously extract newly created Cloudwatch Logs, transform them and 
load them to Elastic cloud for analytics purposes.

![Alt text](images/design1.png?raw=true "Title")


### Design 2:
1. Use AWS Lambda to extract data from different sources such as AWS and Balena
clouds where data is transformed and aggregated for monitoring and alerting purposes.

![Alt text](images/design2.png?raw=true "Title")


### Lessons Learned :
1. It is difficult to differentiate between error logs during log processing and filtering. 
There needs to be a better backend logging system that assigns unique codes to each error.

2. It is costly to run EC2 instances for real-time data processing compared with scheduled 
Lambdas which tend to be a cheaper solution for data that does not require frequent access.

3. The quality of data depends mainly on the processing and aggregation steps. Enhance these
steps further.

### Future Improvements:
1. Enhance log processing through better info/error logs.
2. Monitor the health of Docker containers and Kubernetes pods.
