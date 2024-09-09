# Welcome to the area Cloud Computing wurh docker :whale:
![ReferenceImage](/images/💻 Monitoring🐋.png)

## Relationed CloudComputing
Grafana and Prometheus are monitoring and visualization tools that integrate to provide detailed insight into system performance and health. Prometheus is responsible for collecting and storing time-series metrics, while Grafana is used to visualize this data in interactive dashboards.

As in cloud computing, Grafana and Prometheus enable real-time monitoring and analysis, making it easy to observe resources and applications. In the cloud, services such as AWS CloudWatch or Google Cloud Monitoring offer similar functionalities for collecting and visualizing metrics and logs.

Scalability is another point of agreement. Grafana and Prometheus can handle large volumes of data and scale on demand, comparable to how cloud services automatically scale resources to handle varying loads.

# With Grafana and Prometheus Monitoring is being simple
![ReferenceImage](/images/GrafaP.png)

In today's world, metrics collection is mandatory in order to effective monitoring. To do so, it is quite common to use [Prometheus](https://prometheus.io) and [Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/).

[Prometheus](https://prometheus.io) is a powerful metrics collection and alerting system, and [Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/) is one of the best visualization tools which can be used with Prometheus.

We can create a dashboard with multiple charts together in Grafana.


## *Grafana*

`docker pull grafana/grafana`
### Ports
3000:3000
#### [DockerHub-Image/Grafana](https://hub.docker.com/r/grafana/grafana?uuid=9E4A6F83-9251-4C93-B16E-CF90CF11B843)

## *Prometheus*

`docker pull prom/prometheus`

Then we need to run the container with this section 

`docker run -d \ -v /usr/share/OwnCloud/Monitoring/Prometheus/prometheus.yml:/etc/prometheus prometheus.yml \
  prom/prometheus
`
### Ports
9090:9090
#### [DockerHub-Image/Prometheus](https://hub.docker.com/r/prom/prometheus?uuid=9E4A6F83-9251-4C93-B16E-CF90CF11B843)