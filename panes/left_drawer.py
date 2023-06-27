from nicegui     import ui
from dataclasses import dataclass

import tabs

from state import uiobjs

def init():
    with ui.left_drawer(value=False).classes("bg-blue-100") as left_drawer:
        uiobjs.left_drawer = left_drawer

        ui.label("Current tab")

        with ui.tabs().props("vertical") as tab_list:
            uiobjs.tab_list = tab_list
            for tab_def in tabs.__tabs__:
                ui.tab(tab_def.__name__, label=tab_def.label(), icon=tab_def.icon())
    
    return left_drawer