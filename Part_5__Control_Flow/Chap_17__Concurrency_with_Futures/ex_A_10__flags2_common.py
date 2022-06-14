"""Utilities for second set of flag examples.
"""

from http import HTTPStatus
import os
import time
import sys
import string
import argparse
from collections import namedtuple
from enum import Enum


Result = namedtuple('Result', 'status data')

HTTPStatus = Enum('Status', 'ok not_found error')

POP20_CC = ('CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR').split()

DEFAULT_CONCUR_REQ = 1
MAX_CONCUR_REQ = 1

SERVERS = {
    'REMOTE': 'http://flupy.org/data/flags',
    'LOCAL':  'http://localhost:8001/flogs',
    'DELAY':  'http://localhost:8002/flogs',
    'ERROR':  'http://localhost:8003/flogs',
}
DEFAULT_SERVER = 'LOCAL'

DEST_DIR = 'downloads/'
COUNTRY_CODES_FILE = 'country_codes.txt'


def save_flag(img, filename):
    pass

def initial_report(cc_list, actual_req, server_label):
    pass

def final_report(cc_list, counter, start_time):
    pass

def expand_cc_args(every_cc, all_cc, cc_args, limit):
    pass

def process_args(default_concur_req):
    pass

def main(download_many, default_concur_req, max_concur_req):
    pass