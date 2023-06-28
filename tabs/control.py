from nicegui import ui
import logging

from threading import Event

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

    test_knob = ui.knob(value=0.0, min=-1.0, max=1.0, step=0.01, color="grey")
    test_knob_focus = Event()

    def new_value(x):
        log.info(f"Set knob value to {x}")
        if not test_knob_focus.is_set():
            test_knob.set_value(x)
            test_knob.clear()
            test_knob.props("color=green")

            with test_knob:
                ui.label("").bind_text_from(test_knob, "value", lambda v: f"{v}")

    def focus_in_clbk(x):
        test_knob_focus.set()
        test_knob.props("color=blue")
        test_knob.clear()

        with test_knob:
            ui.label("").bind_text_from(test_knob, "value", lambda v: f"{v}")


    def focus_leave_clbk():
        test_knob_focus.clear()
        test_knob.props("color=orange")
        log.info("Focus leave!")
        test_knob.clear()

        with test_knob:
            ui.spinner(size="md")

        mqtt_connection.publish("knob/out", payload = str(test_knob.value))
    
    def knob_value_clbk(data):
        value = float(str(data.decode("ascii")))
        new_value(value)

    test_knob.on("focusin",  focus_in_clbk   )
    test_knob.on("focusout", focus_leave_clbk)

    mqtt_connection.subscribe("knob/in", callback=knob_value_clbk)

    mqtt_connection.subscribe("test_topic", callback = value_clbk)