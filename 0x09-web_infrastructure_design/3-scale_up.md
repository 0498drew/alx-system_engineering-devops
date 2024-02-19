# Add to previous design


[3-scale_up image url](https://imgur.com/gPMBsw7)
* Server: This is the foundational component of the infrastructure. It provides the computing resources necessary to host and run the various services and applications. Without a server, there would be no platform to deploy the different components of the system.

* Load-Balancer (HAProxy): The load-balancer is added to distribute incoming network traffic across multiple servers. In this case, HAProxy is used for its ability to efficiently balance the load among servers in a cluster. By distributing traffic evenly, it helps prevent any single server from becoming overwhelmed, thus improving the overall performance and reliability of the system. Additionally, HAProxy can perform health checks on servers to ensure they are available and responsive, further enhancing the system's resilience.

* Web Server: The web server is responsible for serving static content (e.g., HTML, CSS, JavaScript files) to clients over the internet. It handles incoming HTTP requests and responds with the appropriate web pages or resources. Separating the web server from the application server allows for better resource utilization and scalability, as each component can be scaled independently based on demand.

* Application Server: The application server hosts the dynamic components of the system, such as business logic, application code, and APIs. It processes incoming requests, interacts with databases or other backend services, and generates dynamic content to be served by the web server. By separating the application logic from the web server, it enables better modularization of the system and facilitates scalability and maintainability.

* Database Server: The database server stores and manages the persistent data used by the application. It provides functionalities for data storage, retrieval, and manipulation, ensuring data integrity and consistency. Separating the database server from the other components allows for better performance optimization, security management, and scalability. It also helps in isolating potential issues or failures related to database operations, minimizing the impact on other parts of the system.
