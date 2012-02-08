#!/usr/bin/env python
"""simpleweb.py: simple web framework"""

__version__ = '0.02'
__author__ = [
    'Jake Kupersmith <jakerosoft@gmail.com>',
    ]
__license__ = 'public domain'

from application import application
from template import widget, document
from webapi import ctx
