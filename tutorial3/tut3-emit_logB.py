#!/usr/bin/env python
import pika
import sys
import time
import os

credentials = pika.PlainCredentials('ccm_dev', 'ec6tv0p5id2sw0cz')

conn_parameters = pika.ConnectionParameters(host='localhost', 
											port=5672, 
											virtual_host='ccm_dev_vhost',
											credentials=credentials)

connection = pika.BlockingConnection(conn_parameters)
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')


for x in range(100000):
	message = "Erik this is message {0} this is process id: {1}".format(x, os.getpid())
	channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
	#print " [x] Sent %r" % (message,)
	#time.sleep(1)

connection.close()