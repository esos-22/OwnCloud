# syntax=docker/dockerfile:1
FROM rabbitmq:4.0-rc-alpine
# plugins to watch rabbitmq on localhost:15672
RUN rabbitmq-plugins enable rabbitmq_management

#local env variables
ENV RABBITMQ_DEFAULT_USER=admin
ENV RABBITMQ_DEFAULT_PASS=password

#volume
VOLUME /var/lib/rabbitmq
EXPOSE 5671 15672
