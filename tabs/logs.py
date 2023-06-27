from nicegui import ui
import logging

from state import uiobjs


log = logging.getLogger("Logs tab")

def label():
    return "Logs"

def icon():
    return "dvr"

def content():
    log_area      = ui.log().classes("w-full h-20")
    uiobjs.log_area = log_area