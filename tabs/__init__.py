####################################
# Define tab list
####################################
from . import control
from . import logs
__tabs__ = [
    control,
    logs,
]

__default_tab__ = control


####################################
# Init function
####################################

def init():
    from nicegui import ui 
    from state   import uiobjs

    # Init tab panes
    with ui.tab_panels(uiobjs.tab_list, value=__default_tab__.__name__):
        for tab_def in __tabs__:
            with ui.tab_panel(tab_def.__name__):
                # Tab title
                ui.markdown(f"#### {tab_def.label()}")
                tab_def.content()