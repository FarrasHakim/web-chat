#!/usr/bin/env python
import pika
import sys
import time
from datetime import datetime

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

exchangemq = "time"
queueName = "timequeue"
channel.exchange_declare(exchange=exchangemq, exchange_type='direct', durable=True)
channel.queue_declare(queue=queueName, durable=True)
channel.queue_bind(queueName, exchangemq)

while True:
    message = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    channel.basic_publish(exchange=exchangemq,
                        routing_key=queueName,
                        body=message)
    print(" [x] Sent %r" % message)
    time.sleep(60) # sleep 1 minute

connection.close()