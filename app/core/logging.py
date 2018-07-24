import datetime
import logging
import sys

from pythonjsonlogger import jsonlogger

from config import LOG_LEVEL


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['timestamp'] = datetime.datetime.now()
        log_record['level'] = record.levelname
        log_record['pathname'] = record.pathname
        log_record['lineno'] = record.lineno


def setup_logging():
    # Nastaveni logovani, original je ten implicitni, ten se pak preadapterovava.
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(CustomJsonFormatter())
    handler.setLevel(LOG_LEVEL)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(LOG_LEVEL)
