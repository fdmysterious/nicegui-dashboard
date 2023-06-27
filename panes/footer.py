from nicegui import ui
from state   import uiobjs

def init():
    with ui.footer() as footer:

        status_label = ui.markdown()

        ui.element("q-space")

        # TODO # Indicators
        ui.icon("circle", color="red")
        ui.label("Status 1")

        ui.icon("circle", color="green")
        ui.label("Status 2")

    uiobjs.footer = footer
    uiobjs.status_label = status_label