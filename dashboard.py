from nicegui import ui
import logging

from dataclasses import dataclass

import tabs
import panes

from state import uiobjs

class NiceLogHandler(logging.Handler):
    def __init__(self, status_label):
        super().__init__()

        self.status_label = status_label

    def emit(self, record):
        log_entry = self.format(record)
        #self.log.push(log_entry)
        status_label.set_text(record.msg)

log = logging.getLogger(__file__)
log.setLevel(logging.DEBUG)

def panic():
    ui.notify("PANIC MODE ACTIVATED!!!")

############################################
# Main app
############################################

with ui.header().classes(replace="row items-center") as header:
    ui.button(on_click = lambda: uiobjs.left_drawer.toggle()).props('flat color=white icon=menu')
    ui.label("Test dashboard")

with ui.footer() as footer:
    status_label = ui.label("")
    ui.element("q-space")
    ui.icon("circle", color="red")
    ui.label("Status 1")
    ui.icon("circle", color="green")
    ui.label("Status 2")

panes.left_drawer.init()
tabs.init()

with ui.page_sticky(position="bottom-right", x_offset=20, y_offset=20):
    ui.button("Panic", color="red", icon="error", on_click=panic)

# Bind logger to UI
logging.basicConfig(level=logging.DEBUG)
root_log    = logging.getLogger("")
log_handler = NiceLogHandler(status_label)
formatter   = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)
root_log.addHandler(log_handler)

ui.run()