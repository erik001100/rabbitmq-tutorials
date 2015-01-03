#!/usr/bin/env python
import pika
import sys


credentials = pika.PlainCredentials('ccm_dev', 'ec6tv0p5id2sw0cz')

conn_parameters = pika.ConnectionParameters(host='localhost', 
											port=5672, 
											virtual_host='ccm_dev_vhost',
											credentials=credentials)

connection = pika.BlockingConnection(conn_parameters)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print " [x] Sent %r" % (message,)
connection.close()