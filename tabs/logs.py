from nicegui import ui
import logging

log = logging.getLogger("Logs tab")

def label():
    return "Logs"

def icon():
    return "dvr"

def content():
    ui.markdown("**TODO**")