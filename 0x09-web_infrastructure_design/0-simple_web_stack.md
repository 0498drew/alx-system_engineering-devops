# Design a one server web infrastructure that hosts the website www.foobar.com
## start your explanation by having a user wanting to access your website
[0-simple_web_stack image url](https://imgur.com/8aWZGEP)

* Server: This is a physical or virtual machine responsible for hosting all components of the web infrastructure.

* Web Server (Nginx): Nginx will handle incoming HTTP requests and serve static content. It will also act as a reverse proxy to pass dynamic requests to the application server.

* Application Server: This is where the dynamic code of the website runs. It interprets requests, processes them, and generates dynamic content to be sent back to the user. For simplicity, let's assume it's running a PHP application, which will be interpreted by PHP-FPM.
* Application Files: This includes all the codebase of the website. For example, HTML, CSS, JavaScript, and PHP files.
* Database (MySQL): MySQL will store and manage the website's data. This includes user accounts, articles, product details, etc.

## Specifics Explained:

* Server: A server is a computer system that provides resources, data, services, or programs to other computers or users over a network.
* Domain Name: The domain name, in this case, foobar.com, serves as a human-readable address to access the website. It's translated to an IP address by the Domain Name System (DNS).
* DNS Record: The www DNS record in www.foobar.com is a subdomain that points to the server's IP address (e.g., 8.8.8.8).
* Web Server (Nginx): The web server handles incoming HTTP requests from clients (browsers) and serves static content. It also acts as a reverse proxy to forward dynamic requests to the application server.
* Application Server: The application server executes the application code (e.g., PHP) in response to dynamic requests. It interacts with the database to retrieve or store data and generates dynamic content for the web server to serve.
* Database: The database stores and manages the website's data. MySQL, in this case, handles tasks such as storing user information, product details, and other relevant data.
* Communication: The server communicates with the user's computer over the internet using the HTTP(S) protocol. When a user requests the website www.foobar.com, their browser sends an HTTP request to the server's IP address. The server processes this request, retrieves necessary data from the database, executes any dynamic code, and sends back an HTTP response containing the requested webpage.

## Issues with the Infrastructure:

* Single Point of Failure (SPOF): Since all components are hosted on a single server, if the server fails, the entire website goes down.
* Downtime during Maintenance: Performing maintenance tasks, such as deploying new code or restarting the web server, may lead to downtime, causing inconvenience to users.
* Limited Scalability: If the website experiences a sudden surge in traffic, a single server may not be able to handle the load efficiently, leading to performance issues or downtime.
