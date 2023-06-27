import logging

class NiceStatusHandler(logging.Handler):
    """
    Helper class to bind to status label
    """
    def __init__(self, status_label):
        super().__init__()
        self.status_label = status_label

    def emit(self, record):
        emojis = {
            logging.INFO:    "👉",
            logging.WARNING: "📢",
            logging.ERROR:   "💀",
        }

        format_fkts = {
            logging.INFO:    lambda s: s,
            logging.WARNING: lambda s: f"*{s}*",
            logging.ERROR:   lambda s: f"**{s}**",
        }
        # Log only messages above info level
        if record.levelno >= logging.INFO:
            self.status_label.set_content(f"{emojis.get(record.levelno, '')} {format_fkts.get(record.levelno, lambda s: s)(record.msg)}")

class NiceLogHandler(logging.Handler):
    """
    Helper class to bind to log object
    """
    def __init__(self, log_area):
        super().__init__()
        self.log_area = log_area

    def emit(self, record):
        log_entry = self.format(record)
        self.log_area.push(log_entry)


def init():
    from state import uiobjs

    # Bind logger to UI
    logging.basicConfig(level=logging.DEBUG)
    formatter   = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    root_log    = logging.getLogger("")
    status_handler = NiceStatusHandler(uiobjs.status_label)

    log_handler    = NiceLogHandler(uiobjs.log_area)
    log_handler.setFormatter(formatter)

    root_log.addHandler(status_handler)
    root_log.addHandler(log_handler   )