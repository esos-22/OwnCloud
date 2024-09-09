# Welcome to the area Cloud Computing wurh docker :whale:
![ReferenceImage](/images/📡 Proxy🐋.png)

## *We  recommended use Nginx*
![ReferenceImage](/images/Nginx.png)
nginx-proxy sets up a container running in nginx and *docker-hen*. Docker-gen generates preverse proxy configs for nginx and reloads nginx when containers are started and stopped.

## Relationed CloudComputing
 Nginx and cloud computing share similarities in traffic management and scalability. Nginx, as a reverse proxy, distributes traffic between backend servers, similar to how load balancers in the cloud distribute requests between instances. Both allow applications to scale: Nginx does this by adding more containers in Docker, while in the cloud they automatically scale based on demand. Additionally, Nginx and cloud services allow for advanced traffic control, with Nginx managing redirects and caching policies, and the cloud offering tools like API Gateway for routing and security. Both also facilitate deployment in container environments, with Nginx operating in Docker and the cloud supporting platforms like Kubernetes for application management.

#### [DockerHub-Image](https://hub.docker.com/_/nginx?uuid=9E4A6F83-9251-4C93-B16E-CF90CF11B843)

# Usage
In Docker Hub we will search "NGINX" and the first option with 1B pulls,  located in the Folder when we re gonna created put 

`docker pull nginx:stable-alpine3.20-perl ` or `docker pull nginx:latest ` 

Then we're gonna created another folder where we're gonna configure our nginx, inside we will create a file *index.html*

# DockerFile
![ReferenceImage](/images/Screen1.png)

### Volume
Volumes in Docker are used to persist data beyond the lifecycle of a container. In the case of Nginx, you might want to use volumes to store configuration files, SSL certificates, logs, or any other resources that Nginx needs to access.

`docker run -d -v /OwnCloud/docker1/nginx.conf:/etc/nginx/nginx.conf -p 80:80 index.html
`
## Ports
8080:80
