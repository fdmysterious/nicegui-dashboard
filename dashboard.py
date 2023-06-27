from nicegui import ui
import logging

from dataclasses import dataclass

class NiceLogHandler(logging.Handler):
    def __init__(self, log, status_label):
        super().__init__()

        self.log          = log
        self.status_label = status_label

    def emit(self, record):
        log_entry = self.format(record)
        self.log.push(log_entry)
        status_label.set_text(record.msg)

log = logging.getLogger(__file__)
log.setLevel(logging.DEBUG)

def panic():
    ui.notify("PANIC MODE ACTIVATED!!!")

@dataclass
class ValueStorage:
    test_value: float = 0.0

############################################
# Main app
############################################

#############
values = ValueStorage()
#############

with ui.header().classes(replace="row items-center") as header:
    ui.button(on_click = lambda: left_drawer.toggle()).props('flat color=white icon=menu')
    ui.label("Test dashboard")

with ui.footer() as footer:
    status_label = ui.label("")
    ui.element("q-space")
    ui.icon("circle", color="red")
    ui.label("Status 1")
    ui.icon("circle", color="green")
    ui.label("Status 2")

with ui.left_drawer(value=False).classes("bg-blue-100") as left_drawer:
    ui.label("Side menu")
    with ui.tabs().props("vertical") as tabs:
        tab_ctrl = ui.tab("Control", icon="build")
        tab_logs = ui.tab("Logs", icon="dvr")

with ui.page_sticky(position="bottom-right", x_offset=20, y_offset=20):
    ui.button("Panic", color="red", icon="error", on_click=panic)

with ui.tab_panels(tabs, value="A").classes("w-full"):
    with ui.tab_panel(tab_ctrl):
        ui.label("Content of A")
        ui.button("Click me!",
            on_click= lambda: log.info(f"This is info message!, current value is {values.test_value}")
        )
        test_knob = ui.knob(show_value=True)
        test_knob.on_value_change = lambda x: log.info(f"Knob changed to {x}")

        ui.button("Click me!", on_click=lambda: ui.notify("Hello world!"))

    with ui.tab_panel(tab_logs):
        ui.label("Logs")
        ui_log = ui.log(max_lines=256).classes("w-full h-20")

# Bind logger to UI
logging.basicConfig(level=logging.DEBUG)
root_log    = logging.getLogger("")
log_handler = NiceLogHandler(ui_log, status_label)
formatter   = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)
root_log.addHandler(log_handler)

ui.run()