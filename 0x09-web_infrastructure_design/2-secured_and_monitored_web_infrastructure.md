![2-secured_and_monitored_web_infrastructure image url](https://imgur.com/6QxpfTu)
## Components:

### Firewalls (3):
* Purpose: Act as a barrier between the internal network (servers) and the external network (internet), filtering incoming and outgoing traffic to prevent unauthorized access and protect against various cyber threats.

### SSL Certificate:
* Purpose: Encrypts data exchanged between clients (browsers) and the server, ensuring confidentiality and integrity of sensitive information transmitted over the network.

### Monitoring Clients (3):
* Purpose: Collect data about the health, performance, and security of the infrastructure, enabling proactive detection and resolution of issues.

## Specifics:

### Firewalls:
* Added to control and secure incoming and outgoing traffic.
* HTTPS: Traffic is served over HTTPS to encrypt data transmission, preventing eavesdropping, tampering, and man-in-the-middle attacks.

### Monitoring:
* Used to track various metrics such as server health, resource utilization, network activity, and security events.
* Monitoring Tool (e.g., Sumo Logic) collects data from monitoring clients to provide insights into the performance and security of the infrastructure.

### Monitoring Data Collection:
* Monitoring clients gather data from various sources, including server logs, system metrics, network traffic, and security events.

### Monitoring Web Server QPS:
* To monitor web server Query Per Second (QPS), one can configure monitoring clients to collect and analyze web server access logs or utilize server metrics to track the number of incoming requests per second.

## Issues with the Infrastructure:
### Terminating SSL at Load Balancer:
* Terminating SSL at the load balancer exposes decrypted traffic within the internal network, potentially compromising data confidentiality if the internal network is breached.
### Single MySQL Server for Writes:
* Having only one MySQL server capable of accepting writes introduces a single point of failure and limits scalability, as increased write traffic can overwhelm the server and degrade performance.
### Identical Servers:
* Deploying servers with identical components increases the risk of widespread failures if a vulnerability or issue affects all servers simultaneously. It also lacks diversity in the event of targeted attacks or software bugs affecting specific components.
