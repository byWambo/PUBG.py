# -*- coding: utf-8 -*-

"""
PUBG.py
---------

A Python Wrapper of the PUBG API.
This Library is under development. So please don't except to much.

:copyright: (c) 2018 Matthias K.
"""

__title__ = "PUBG.py"
__author__ = "Matthias K."
__version__ = '0.0.1a'
__copyright__ = '(c) 2018 Matthias K.'
__url__ = 'https://github.com/byWambo/PUBG.py'

import logging
import sys

from pubg.http import *

fmt = '[%(levelname)s] %(asctime)s - %(name)s:%(lineno)d - %(message)s'
logging.basicConfig(format=fmt, level=logging.INFO)

# To support Python versions under 3.6.1, we need to implement our own NullHandler
try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

if sys.version_info < (3, 4):
    raise RuntimeError('Upgrade your Python! 3.6.5 is recommend.')
