import os
import re

REGISTER_REGEXP = re.compile(r'^\$register: ([0-9A-z]{8})$')
ROOT = os.path.dirname(os.path.abspath(__file__))
HOST = os.getenv('HOST', '0.0.0.0')
PORT = os.getenv('PORT', 8080)

PB_DEBUG = os.getenv('PB_DEBUG', True)
