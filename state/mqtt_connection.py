"""
=================
MQTT client stuff
=================
"""

import paho.mqtt.client as mqtt
import logging

conn            = None   # Global object representing client connection
routes          = dict() # Topic/callback

log = logging.getLogger("mqtt_connection")

def __on_message(client, userdata, message):
    topic = message.topic
    data  = message.payload

    # Check if route exist
    log.debug(f"Received {topic}: {data}")

    clbk = routes.get(topic, None)

    if clbk is not None:
        clbk(data)
    else:
        log.warn(f"Received message on topic {topic}, but no associated callback, discarding")


def init(broker_config):
    global conn

    host      = broker_config.get("host",    None)
    port      = broker_config.get("port",    None)
    client_id = broker_config.get("client_id", "")

    log.info(f"Init MQTT broker connection: host = {host}, port = {port}, client_id = {client_id or '<none>'}")

    conn            = mqtt.Client(client_id)
    conn.on_message = __on_message

    conn.connect(host=host, port=port)

def start():
    global conn
    log.debug("Start MQTT loop")

    log.debug("-> Subscribe to registered topics")
    for topic in routes.keys():
        log.debug(f"  : {topic}")
        conn.subscribe(topic, qos=0) # Keep qos=0 by default

    conn.loop_start()

def stop():
    global conn
    log.debug("Stop MQTT loop")
    conn.loop_stop()

def subscribe(topic, callback, qos=0):
    log.debug(f"Subscribe to topic {topic}")

    if topic in routes:
        raise RuntimeError(f"Already subscribed to topic {topic}")

    routes[topic] = callback

    if conn is not None:
        conn.subscribe(topic, qos)

def publish(topic, payload=None, qos=0, retain=False):
    log.debug(f"Publish to {topic}: {payload}, with qos={qos} and retain={retain}")
    if conn is not None:
        conn.publish(topic=topic, payload=payload, qos=qos, retain=retain)
    else:
        log.warning(f"Cannot publish on topic {topic}, as MQTT client is not init.")