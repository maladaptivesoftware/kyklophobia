import logging

WSRC = 26
WLVL = 8

class Format(logging.Formatter):
    def format(self, record):
        t   = self.formatTime(record, "%H:%M:%S")
        src = f"{record.filename}:{record.lineno}"
        if len(src) > WSRC:
            src = src[-WSRC:]
        msg = record.getMessage()
        if record.exc_info:
            msg += "\n" + self.formatException(record.exc_info)
        return f"{t} {src:<{WSRC}} {record.levelname:<{WLVL}} {msg}"

def setup(level=logging.INFO):
    h = logging.StreamHandler()
    h.setFormatter(Format())
    logging.root.handlers = [h]
    logging.root.setLevel(level)
