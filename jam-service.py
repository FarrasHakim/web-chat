#!/usr/bin/env python
import pika
import sys
import time
from datetime import datetime

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='time')

while True:
    message = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    channel.basic_publish(exchange='', routing_key='time', body=message)
    print(" [x] Sent %r" % message)
    time.sleep(60) # sleep 1 minute

connection.close()