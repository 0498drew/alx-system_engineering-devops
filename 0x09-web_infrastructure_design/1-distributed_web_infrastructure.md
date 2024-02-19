# Design a three server web infrastructure that hosts the website www.foobar.com
[1-distributed_web infrastucture image url](https://imgur.com/BHster)
## Components:

### Load Balancer (HAproxy):
  * Purpose: Distribute incoming traffic evenly across multiple servers for load balancing and high availability.
  * Distribution Algorithm: Round Robin (Simple and efficient method, distributes requests equally among servers in a circular manner).
  * Active-Active Setup: Both servers are actively serving traffic, distributing the load and providing redundancy in case of failure.

### Web Server (Nginx):
  * Purpose: Serve static content, handle incoming HTTP requests, and act as a reverse proxy for dynamic content.
  * Active-Active Setup: Both servers are actively serving requests.

### Application Server:
  * Purpose: Execute server-side code, process dynamic content requests from the web server, and communicate with the database.
  * Active-Active Setup: Both servers are actively processing application logic and handling requests.

### Set of Application Files (Code Base):
  * Purpose: Contains the application code to be executed on the application servers.

### Database (MySQL):
  * Purpose: Store and manage website data.
  * Primary-Replica (Master-Slave) Cluster: Primary node handles both read and write operations, while replica nodes replicate data from the primary node to provide redundancy and handle read-only queries.

## Specifics:

* Load Balancer Algorithm: Round Robin - Distributes requests evenly among servers, preventing any single server from becoming overwhelmed.
* Database Primary-Replica Cluster: Primary node handles write operations, ensuring data consistency, while replica nodes handle read operations, offloading read traffic from the primary node and providing fault tolerance.

### Difference between Primary and Replica Nodes:
* Primary Node: Handles write operations and serves as the authoritative source for data modifications.
* Replica Node: Replicates data from the primary node and serves read-only queries, reducing the load on the primary node and providing fault tolerance.

## Issues with the Infrastructure:

### Single Points of Failure (SPOF):
* The absence of redundancy in critical components like the load balancer, web server, application server, and database creates single points of failure.

### Security Issues:
* Lack of firewall exposes the infrastructure to potential attacks.
* Absence of HTTPS encryption leaves data vulnerable to interception and manipulation.
###No Monitoring:
* Without monitoring tools, it's challenging to detect and troubleshoot issues promptly, leading to potential downtime and performance degradation.
