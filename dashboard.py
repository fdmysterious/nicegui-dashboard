from state import mqtt_connection
from state import uiobjs

#########################

import logging
from dataclasses import dataclass

from nicegui import ui
import coloredlogs

import config
import panes
import utils

log = logging.getLogger("dashboard")
log.setLevel(logging.DEBUG)

def panic():
    log.error("PANIC MODE ACTIVATED!!!")
    ui.notify("PANIC MODE ACTIVATED!!!")

############################################
# Main app
############################################
coloredlogs.install(level=logging.DEBUG)


############################################
# Load config
############################################
config.load()


############################################
# UI Init
############################################

with ui.header().classes(replace="row items-center") as header:
    ui.button(on_click = lambda: uiobjs.left_drawer.toggle()).props('flat color=white icon=menu')
    ui.label("Test dashboard")

panes.footer.init()
panes.left_drawer.init()
panes.tabs.init()

with ui.page_sticky(position="bottom-right", x_offset=20, y_offset=20):
    ui.button("Panic", color="red", icon="error", on_click=panic)

############################################
# Post-ui init
############################################
if __name__ == "__mp_main__":
    utils.log.init()

    mqtt_connection.init(config.get("mqtt.broker"))
    log.info("Hello world!")

    mqtt_connection.start()

ui.run(dark=True, title=config.get("dashboard.title") or "Dashboard")