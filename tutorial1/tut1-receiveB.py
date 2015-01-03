#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('ccm_dev', 'ec6tv0p5id2sw0cz')

conn_parameters = pika.ConnectionParameters(host='localhost', 
											port=5672, 
											virtual_host='ccm_dev_vhost',
											credentials=credentials)

connection = pika.BlockingConnection(conn_parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received body: {0} properties: {1} method: {2} ch: {3}".format(body, properties, method, ch)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()