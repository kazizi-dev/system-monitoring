# system-monitoring
System monitoring with the help of Python, Elastic ELK stack, AWS, and Docker.

### Motivation:
Build a monitoring and analytical system that can support internal teams with data inquiries. Equip the system with automated alerts and tickets to reduce team overhead.

### Objectives:
1. Design real-time and scheduled data processign solutions that collect and aggregate data.
2. Build a system that can alert the team about problems and anomalies on Slack.
3. Create an automated ticketing system on Jira.

### Phase 1:
1. Install a Logstash image in a docker container and run the container using an EC2 instance on AWS cloud to continously extract newly created Cloudwatch Logs.
2. Transform these logs and load them to Elastic cloud for monitoring purposes.

![Alt text](images/design1-overview.png?raw=true "Title")


### Phase 2:
1. Use AWS Lambda to extract data from different sources such as AWS and Balena clouds.
2. Transform and aggregate data for monitoring and alerting purposes.

![Alt text](images/design2-overview.png?raw=true "Title")


### Phase 3:
1. Extract web app metrics by using Elastic Application Performance Monitoring (APM). Use the metrics to monitor user clicks, API and web page latencies.
2. Extract Docker metrics by using Elastic Metricbeat. These metrics will tell us information such as uptime, resource usage, and any errors.

![Alt text](images/design3-overview.png?raw=true "Title")

### Lessons Learned :
1. It is difficult to differentiate between error logs during log processing and filtering. There needs to be a better backend logging system that assigns unique codes to each error. That way it is easier to process and filter logs for alerting purposes.

2. AWS secheduled Lambdas are far cheaper than running AWS EC2 instances for processing data that is not accessed frequently.

3. The quality of data depends mainly on the initial preprocessing and aggregation steps. Enhance these steps further.

### Future Improvements:
1. Enhance error logs by using specific error codes, so warnings and severe bugs can be differentiated.
2. Monitor the health of Docker containers and Kubernetes pods in near real time.
