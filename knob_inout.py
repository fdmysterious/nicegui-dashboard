"""
Simple service to transmit in value to out for knob
"""

import time
import logging
import coloredlogs

import paho.mqtt.client as mqtt

coloredlogs.install(level=logging.DEBUG)
log = logging.getLogger("knob-inout")

log.info("Hello world!")

def on_message(client, usrdata, message):
    log.info("Received value, retransmitting to knob/in topic")

    topic   = message.topic
    payload = message.payload
    time.sleep(0.2)
    client.publish("knob/in", payload, qos=0)

client = mqtt.Client("knob-inout")
client.on_message = on_message

client.connect(host="localhost", port=1883)

client.subscribe("knob/out")
client.loop_forever()
