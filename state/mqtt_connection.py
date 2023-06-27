"""
=================
MQTT client stuff
=================
"""

import paho.mqtt.client as mqtt
import logging

conn            = None                            # Global object representing client connection
process_message = lambda topic,usrdata,data: None # Process message callback

log = logging.getLogger("mqtt_connection")

def __on_message(*args):
    process_message(*args)

def init(broker_config):
    global conn

    host      = broker_config.get("host",    None)
    port      = broker_config.get("port",    None)
    client_id = broker_config.get("client_id", "")

    log.info(f"Init MQTT broker connection: host = {host}, port = {port}, client_id = {client_id or '<none>'}")

    conn      = mqtt.Client(client_id)

    conn.connect(host=host, port=port)
    conn.on_message = __on_message

def set_message_callback(x):
    global process_message
    process_message = x

def start():
    global conn
    log.debug("Start MQTT loop")
    conn.loop_start()

def stop():
    global conn
    log.debug("Stop MQTT loop")
    conn.loop_stop()