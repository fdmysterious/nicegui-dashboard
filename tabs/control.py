from nicegui import ui
import logging

log = logging.getLogger("Control tab")

def label():
    return "Control"

def icon():
    return "build"

def content():
    ui.button("Click me!", on_click=lambda: log.info("This is info message!"))