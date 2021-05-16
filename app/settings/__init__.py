import contextlib

with contextlib.suppress(ImportError):
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())  # load environment variables from .env when using pycharm


from .base import *
from .path import *
from .apps import *
from .databases import *
from .languages import *
from .drf import *
from .logging import *
