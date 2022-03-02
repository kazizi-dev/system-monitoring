# system-monitoring
System monitoring with the help of Python, Elastic ELK stack, AWS, and Docker.

### Motivation:
Build a system that can answer business and technical related questions for engineering and customer support teams in order to better assist clients.

### Objectives:
1. Design real-time and scheduled data processign solutions that collect and aggregate data.
2. Build a system that can alert the team about problems and anomalies on Slack.
3. Create an automated ticketing system on Jira.

### Design 1:
1. Install a Logstash image in a docker container and run the container using an EC2 instance on AWS cloud to continously extract newly created Cloudwatch Logs.
2. Transform these logs and load them to Elastic cloud for monitoring purposes.

![Alt text](images/design1-overview.png?raw=true "Title")


### Design 2:
1. Use AWS Lambda to extract data from different sources such as AWS and Balena clouds.
2. Transform and aggregate data for monitoring and alerting purposes.

![Alt text](images/design2-overview.png?raw=true "Title")


### Design 3:
1. Extract web app metrics by using Elastic Application Performance Monitoring (APM). Use the metrics to monitor user clicks, API and web page latencies.
2. Extract Docker metrics by using Elastic Metricbeat. These metrics will tell us information such as uptime, resource usage, and any errors.

![Alt text](images/design3-overview.png?raw=true "Title")

### Lessons Learned :
1. It is difficult to differentiate between error logs during log processing and filtering. There needs to be a better backend logging system that assigns unique codes to each error. That way it is easier to process and filter logs for alerting purposes.

2. It is costly to run EC2 instances for real-time data processing compared with scheduled Lambdas which tend to be a cheaper solution for data that does not require frequent access.

3. The quality of data depends mainly on the initial processing and aggregation steps. Enhance these steps further.

### Future Improvements:
1. Enhance log processing through better info/error logs.
2. Monitor the health of Docker containers and Kubernetes pods.
