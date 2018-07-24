import logging

from raven.conf import setup_logging
from raven.handlers.logging import SentryHandler

from app.config import SENTRY_DSN

# Sentry logging setup (optional)
if SENTRY_DSN:
    sentry_handler = SentryHandler(SENTRY_DSN, tags={'component': "flask_app"})
    sentry_handler.setLevel(logging.ERROR)
    setup_logging(sentry_handler)
