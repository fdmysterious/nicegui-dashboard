####################################
# Init function
####################################

def init():
    from nicegui import ui 
    from state   import uiobjs

    import tabs


    # Init tab panes
    with ui.tab_panels(uiobjs.tab_list, value=tabs.__default_tab__.__name__).classes("w-full"):
        for tab_def in tabs.__tabs__:
            with ui.tab_panel(tab_def.__name__).classes("w-full"):
                # Tab title
                ui.markdown(f"#### {tab_def.label()}")
                tab_def.content()