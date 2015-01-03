#!/usr/bin/env python
import pika
import time


credentials = pika.PlainCredentials('ccm_dev', 'ec6tv0p5id2sw0cz')

conn_parameters = pika.ConnectionParameters(host='localhost', 
											port=5672, 
											virtual_host='ccm_dev_vhost',
											credentials=credentials)

connection = pika.BlockingConnection(conn_parameters)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep( body.count('.') )
    print " [x] Done"
    print "Method Delivery Tag is: {0}".format(method.delivery_tag)
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()