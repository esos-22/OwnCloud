import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                               port=5672,
                                                               credentials=pika.PlainCredentials('admin', 'password')))
channel = connection.channel()
channel.queue_declare(queue = 'hi')

channel.basic_publish(exchange='', routing_key='hi',body='hellow')
print ('[x]sent hellow')
connection.close()