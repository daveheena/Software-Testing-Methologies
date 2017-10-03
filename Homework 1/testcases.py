# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 19:39:19 2017

@author: Heena
"""

import unittest
import requests

def parse_service_call(expression,expected_value):
    
    if not type(expression) is str:
        return None
    if expression == None:
        expression = "None"
    expression = str(expression)
    result = requests.get("http://localhost:8080/scientific_notation/"+expression)
    if result.status_code != 200:
        return None
    assert 'json' in result.headers['Content-Type']
    data = result.json()
    #print data['value']
    assert str(data['value']) == str(expected_value)

class Parser_TestService(unittest.TestCase):
    def test_1_check_scientific_notation(self):
        parse_service_call("0.05","5.0 * 10^-2")
        parse_service_call("0.1234","1.234 * 10^-1")
        parse_service_call("0.00000567","5.67 * 10^-6")
        
    def test_2_check_scientific_notation(self):    
        parse_service_call(1.23,"None")
        parse_service_call(0,"None")
        parse_service_call(5,"None")
        
    def test_3_check_scientific_notation(self):    
        parse_service_call(".0051","5.1 * 10^-3")
        parse_service_call(".5","5.0 * 10^-1")
        parse_service_call(".5500001","5.500001 * 10^-1")
        
    def test_4_check_scientific_notation(self):    
        parse_service_call(".00.51","None")
        parse_service_call(".5@","None")
        parse_service_call(".5500001%1","None")
        
    def test_5_check_scientific_notation(self):    
        parse_service_call("1234","1.234 * 10^3")
        parse_service_call("12.34","1.234 * 10^1")
        parse_service_call("1234.0001","1.2340001 * 10^3")
        
    def test_6_check_scientific_notation(self):    
        parse_service_call("1.2.34","None")
        parse_service_call("12.34@","None")
        parse_service_call("1234.000.1%","None")
        parse_service_call("","None")
        
    def test_7_check_scientific_notation(self):    
        parse_service_call("-1234","-1.234 * 10^3")
        parse_service_call("-12.34","-1.234 * 10^1")
        parse_service_call("-1234.0001","-1.2340001 * 10^3")
        
    def test_8_check_scientific_notation(self):
        parse_service_call("-0.05","-5.0 * 10^-2")
        parse_service_call("-0.1234","-1.234 * 10^-1")
        parse_service_call("-0.00000567","-5.67 * 10^-6")
        
if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)