# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 19:54:26 2017

@author: Heena
"""

from bottle import route, run

import myparser

@route("/")
@route("/scientific_notation")
@route("/scientific_notation/<expression>")
def evaluate(expression=""):
    value = myparser.parser(expression)
    if value == None:
        value = 'None'
    return {'expression':expression, 'value':value}

run(host='localhost', port=8080)