# system-monitoring-design
System monitoring design with the help of Elastic ELK stack, AWS, and Docker.

### Objectives:
1. Design a real-time and scheduled data processign solution that can monitor logs
and other forms of data coming from AWS and Balena cloud systems.

2. Build a system that can alert the team about problems and anomalies on services
such as Slack, so issues can be investigated faster. Also, create an automated 
ticket for every severe problem and assign it to the right person in the team.  

### Motivation:
Build a system that can answer business and technical related questions for 
engineering and customer support teams in order to better assist clients.


### Design 1:
1. Install a Logstash image in a docker container and run the container using an EC2
instance on AWS cloud to instantly extract new Cloudwatch Logs, transform them and 
load them to Elastic cloud for analytics purposes.


![Alt text](images/design1.png?raw=true "Title")


### Design 2:
1. Use AWS Lambda to extract data from different sources such as AWS cloud and Balena
cloud where the data can be transformed, used for automated alerts/tickets, and other
analytics purposes.


![Alt text](images/design2.png?raw=true "Title")


### Future Improvements:
1. Enhance log processing through better info/error logs.
2. Monitor the health of Docker containers and Kubernetes pods.
3. Automate Index Lifecycle Management (ILM) policies for Elastic cloud.
