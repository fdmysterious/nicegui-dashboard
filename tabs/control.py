from nicegui import ui
import logging

import time

from state import mqtt_connection

log = logging.getLogger("Control tab")

def label():
    return "Control"

def icon():
    return "build"

def content():
    button = ui.button("Click me!")
    def button_onclick():
        mqtt_connection.publish("ui/test_button/click", payload=f"{time.time()}".encode("ascii"))
    button.on("click", button_onclick)

    test_label = ui.label("")
    def value_clbk(x):
        log.info("Received some stuff!")
        test_label.set_text(x.decode("ascii"))

    mqtt_connection.subscribe("test_topic", callback = value_clbk)