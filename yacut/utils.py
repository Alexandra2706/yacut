import random

from yacut.consts import SYMBOLS_FOR_URL, SHORT_SIZE
from yacut.models import URLMap


def get_unique_short_id():
    short = ''.join(random.choices(SYMBOLS_FOR_URL, k=SHORT_SIZE))
    if URLMap.query.filter_by(short=short).first():
        get_unique_short_id()
    return short
