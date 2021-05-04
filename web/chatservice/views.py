from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import pika
import json

# Create your views here.
def index(request):
    sessionId = request.session.get("sessionId")
    if sessionId == None:
        sessionId = randint(0,999999)
        request.session["sessionId"] = sessionId
    context = {
        "sessionId": sessionId
    }
    if (request.method == "POST"):
        message = {
            "sessionId" : sessionId,
            "message" : request.POST.get("message")
        }
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        exchangemq = "chatmessage"
        channel.exchange_declare(exchange=exchangemq, exchange_type='direct', durable=True)

        channel.basic_publish(exchange=exchangemq,
                            routing_key="stream",
                            body=json.dumps(message))
        print(" [x] Sent %r" % message)
        connection.close()
        return HttpResponse("Message Sent")
    return render(request, "index.html", context)