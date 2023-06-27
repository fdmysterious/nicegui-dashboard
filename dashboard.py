from nicegui import ui
import logging

from dataclasses import dataclass

import panes
import utils

from state import uiobjs

log = logging.getLogger(__file__)
log.setLevel(logging.DEBUG)

def panic():
    log.error("PANIC MODE ACTIVATED!!!")
    ui.notify("PANIC MODE ACTIVATED!!!")

############################################
# Main app
############################################

with ui.header().classes(replace="row items-center") as header:
    ui.button(on_click = lambda: uiobjs.left_drawer.toggle()).props('flat color=white icon=menu')
    ui.label("Test dashboard")

#with ui.footer() as footer:
#    status_label = ui.label("")
#    ui.element("q-space")
#    ui.icon("circle", color="red")
#    ui.label("Status 1")
#    ui.icon("circle", color="green")
#    ui.label("Status 2")

panes.footer.init()
panes.left_drawer.init()
panes.tabs.init()

with ui.page_sticky(position="bottom-right", x_offset=20, y_offset=20):
    ui.button("Panic", color="red", icon="error", on_click=panic)

utils.log.init()
log.info("Hello world!")

ui.run()